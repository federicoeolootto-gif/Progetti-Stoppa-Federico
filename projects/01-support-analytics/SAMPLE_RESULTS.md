# Sample Results · Synthetic Support Tickets

These metrics are computed from **60 fabricated tickets** by [`report_demo.py`](report_demo.py). They are presented only to demonstrate how operational questions can be answered consistently; **they are not real business results, client statistics or outcomes from an employer**.

| KPI | Reproducible value | Definition / denominator |
|---|---:|---|
| Ticket records | 60 | Distinct synthetic ticket IDs |
| Closed cases | 48 | Records marked `Closed` with a closure timestamp |
| Open cases | 12 | Records marked `Open` without a closure timestamp |
| Closure share | 80.0% | 48 closed / 60 observed records, **not** a service-level target |
| Cases with an observed first view | 54 | Nonempty `first_viewed_at` |
| Average first-view delay | 4.17 hours | Mean over **54 observed** timestamps only |
| Average resolution time | 67.92 hours | Mean over **48 closed** tickets only |
| Assigned to Support | 32 | Assigned team in the fictional dataset |
| Assigned to BTGuard | 28 | Assigned team in the fictional dataset |

**Interpretation:** Open tickets have unknown resolution times, not zero-hour resolution times. Assignment counts do not prove who actually processed or closed tickets. Metrics reflect the input window and timestamp convention of the synthetic sample.

Reproduce using:

```bash
python projects/01-support-analytics/report_demo.py
```

If the fabricated dataset changes, rerun the script and update this table. No inferential generalization is justified from simulated data.
