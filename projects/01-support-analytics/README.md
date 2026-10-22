# Support Analytics — SQL + Power BI Demonstrator

This folder is a **fully synthetic demonstration**, **not** a copy of any employer's database or dashboards. It models typical operational questions from a support function: ticket volumes, resolution times, workload by team and monthly trends.

This dataset is generated for this public demo. `operator_id` represents a synthetic **assigned operator**, not a verified real-world ticket creator or resolver.

## Quick start (PostgreSQL)

1. Create a PostgreSQL database (free, local).
2. Run `sql/01_schema.sql`.
3. Use your SQL client's CSV Import tool to load `data/support_tickets_synthetic.csv` into `support_tickets`.
4. Run `sql/02_kpis.sql`. On a fresh database, the sample contains **60** distinct tickets (48 closed, 12 open). The schema and metrics are designed for PostgreSQL; run them on PostgreSQL to check full dialect compatibility.
5. Open `data/support_tickets_synthetic.csv` in Power BI Desktop and build the views described in `dashboard_guide.md`.

## Data dictionary

`ticket_id` unique ticket; `customer_id` synthetic customer; `team` Support/BTGuard; `operator_id` pseudonymous synthetic operator; `opened_at`, `first_viewed_at`, `closed_at` timestamps; `category` issue label; `status` open/closed.

## Learning goals

- Explicit KPI definitions; filter consistency; handling missing timestamps.
- `COUNT(*)` vs distinct tickets; resolution and first-response times.
- Grouping by team, customer and time with CTEs and window functions.
- Communicating uncertainty: an open ticket has no observed resolution time.

There are **no employer records, customer data or proprietary formulas** here.
