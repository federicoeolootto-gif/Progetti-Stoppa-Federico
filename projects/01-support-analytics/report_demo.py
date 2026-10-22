"""Self-contained summary of FICTIONAL support tickets; not employer-derived data."""
from __future__ import annotations
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import mean

CSV_PATH = Path(__file__).parent / "data" / "support_tickets_synthetic.csv"
FMT = "%Y-%m-%d %H:%M:%S"


def calculate_report(path: Path = CSV_PATH) -> dict:
    """Report observed timestamps without assuming a resolution time for open tickets."""
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    ids = [r['ticket_id'] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError('Ticket IDs must be unique')
    status_counts = Counter(r['status'] for r in rows)
    if set(status_counts) - {'Open', 'Closed'}:
        raise ValueError('Unexpected ticket status')
    by_team = dict(sorted(Counter(r['team'] for r in rows).items()))
    first_view_hours, resolved_hours = [], []
    for row in rows:
        opened = datetime.strptime(row['opened_at'], FMT)
        first_viewed = datetime.strptime(row['first_viewed_at'], FMT) if row['first_viewed_at'] else None
        closed = datetime.strptime(row['closed_at'], FMT) if row['closed_at'] else None
        if first_viewed is not None:
            hours = (first_viewed - opened).total_seconds() / 3600
            if hours < 0: raise ValueError('First-view timestamp precedes opening')
            first_view_hours.append(hours)
        if row['status'] == 'Open' and closed is not None:
            raise ValueError('Open ticket has a closed timestamp')
        if row['status'] == 'Closed':
            if closed is None: raise ValueError('Closed ticket lacks a closed timestamp')
            hours = (closed - opened).total_seconds() / 3600
            if hours < 0: raise ValueError('Closure precedes opening')
            resolved_hours.append(hours)
    return {
        'tickets': len(rows),
        'closed_tickets': status_counts['Closed'],
        'open_tickets': status_counts['Open'],
        'closure_share_percent': round(100 * status_counts['Closed'] / len(rows), 1) if rows else None,
        'tickets_by_team': by_team,
        'observed_first_views': len(first_view_hours),
        'mean_first_view_hours': round(mean(first_view_hours), 2) if first_view_hours else None,
        'observed_resolutions': len(resolved_hours),
        'mean_resolution_hours_closed_only': round(mean(resolved_hours), 2) if resolved_hours else None,
    }


if __name__ == '__main__':
    from pprint import pprint
    print('Synthetic example — NOT real employer data')
    pprint(calculate_report())
