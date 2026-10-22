"""Unit tests of public examples ONLY. No external API or personal data."""
import csv
import importlib.util
from pathlib import Path
import math
import unittest

ROOT = Path(__file__).resolve().parents[1]


def from_path(relative_path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    mod = importlib.util.module_from_spec(spec)
    # dataclasses resolve the module's name in sys.modules
    import sys
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


GEO = from_path('projects/09-geospatial-weather/spatial_weights.py', 'geo_demo')
FANTA = from_path('projects/03-fantagiungla/public_event_demo.py', 'fanta_demo')


class PublicExampleTests(unittest.TestCase):
    def test_synthetic_ticket_csv(self):
        path = ROOT / 'projects/01-support-analytics/data/support_tickets_synthetic.csv'
        with path.open(encoding='utf-8', newline='') as f:
            records = list(csv.DictReader(f))
        self.assertEqual(len(records), 60)
        self.assertEqual(len({r['ticket_id'] for r in records}), 60)
        self.assertEqual(sum(r['status'] == 'Closed' for r in records), 48)
        self.assertTrue(all((r['status'] == 'Open') == (r['closed_at'] == '') for r in records))
        self.assertTrue(all(r['customer_id'].startswith('Client-') for r in records))

    def test_geo_exact_hit(self):
        self.assertEqual(GEO.weighted_mean((0, 0), [(0, 0, 8), (0.1, 0.2, 10)]), 8)

    def test_geo_out_of_radius(self):
        self.assertIsNone(GEO.weighted_mean((0, 0), [(20, 20, 12)]))

    def test_geo_missing_measurement_is_skipped(self):
        self.assertIsNone(GEO.weighted_mean((0, 0), [(5, 5, None)]))
        self.assertEqual(GEO.weighted_mean((0, 0), [(0, 0, None), (0.2, 0.1, 7)]), 7)

    def test_geo_invalid(self):
        with self.assertRaises(ValueError): GEO.weighted_mean((0, 0), [(math.nan, 10, 3)])
        with self.assertRaises(ValueError): GEO.weighted_mean((0, 0), [], radius_km=0)
        with self.assertRaises(ValueError): GEO.weighted_mean((91, 0), [])

    def test_fanta_idempotency_and_budget(self):
        s = FANTA.AuctionState(budgets={'Team-1': 100, 'Team-2': 100})
        for e in FANTA.sample_events(): self.assertTrue(s.consume(e))
        self.assertFalse(s.consume(FANTA.sample_events()[-1]))
        self.assertEqual(s.budgets['Team-2'], 85)
        self.assertEqual(len(s.purchases), 1)

    def test_fanta_validation_prevents_partial_update(self):
        s = FANTA.AuctionState(budgets={'Team-1': 10})
        with self.assertRaises(ValueError):
            s.consume({'event_id': 'x', 'kind': 'PURCHASE', 'player': 'Player-A', 'team': 'Team-1', 'price': 20})
        self.assertEqual(s.budgets['Team-1'], 10)
        self.assertFalse(s.processed_events)

    def test_auction_refuses_nonleader_and_conflicting_replay(self):
        s = FANTA.AuctionState(budgets={'Team-1': 100, 'Team-2': 100})
        bid = {'event_id': 'b1', 'kind': 'BID', 'player': 'Player-A', 'team': 'Team-1', 'price': 30}
        s.consume(bid)
        with self.assertRaises(ValueError):
            s.consume({'event_id': 'p1', 'kind': 'PURCHASE', 'player': 'Player-A', 'team': 'Team-2', 'price': 31})
        with self.assertRaises(ValueError):
            s.consume({**bid, 'price': 35})
        self.assertEqual(s.budgets, {'Team-1': 100, 'Team-2': 100})
        self.assertEqual(len(s.processed_events), 1)

    def test_ml_demonstrator_outputs_finite(self):
        import numpy as np
        demo = from_path('projects/02-climate-ml/synthetic_ml_demo.py', 'ml_demo')
        values = demo.evaluate()
        self.assertEqual(set(values), {'mean_baseline','decision_tree','random_forest'})
        self.assertTrue(all(np.isfinite(v) and v > 0 for v in values.values()))


if __name__ == '__main__':
    unittest.main()
