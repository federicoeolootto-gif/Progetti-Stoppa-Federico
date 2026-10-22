# Reproduce the public examples

## Requirements

- Python **3.10 or newer** (tested using available local Python runtime)
- Node.js **18 or newer** for the Nova demo
- Internet access to install Python packages, if not already installed
- PostgreSQL 13+ **only** if you choose to run the optional SQL examples

From the **repository root**:

```bash
python -m pip install -r requirements-demos.txt
python -m unittest discover -s tests -v
node --test projects/04-nova/mock_provider.test.cjs
```

Run examples independently:

```bash
python projects/01-support-analytics/report_demo.py
python projects/02-climate-ml/synthetic_ml_demo.py
python projects/03-fantagiungla/public_event_demo.py
python projects/09-geospatial-weather/spatial_weights.py
```

### Support Operations SQL (optional)

Create an empty PostgreSQL database called `portfolio_demo` **on your own machine**, then run from the repository root:

```bash
psql -d portfolio_demo -f projects/01-support-analytics/sql/01_schema.sql
psql -d portfolio_demo -c "\copy support_tickets FROM 'projects/01-support-analytics/data/support_tickets_synthetic.csv' WITH (FORMAT csv, HEADER true)"
psql -d portfolio_demo -f projects/01-support-analytics/sql/02_kpis.sql
```

The SQL scripts have been reviewed for their use of PostgreSQL constructs. **No live PostgreSQL run is claimed in the project audit.** If you repeat the import, clear the demo table first or use a fresh database: `ticket_id` is unique. The precomputed metrics in [SAMPLE_RESULTS](../projects/01-support-analytics/SAMPLE_RESULTS.md) are produced by the included Python script, **not** by a verified PostgreSQL run.

### Key constraints

- This repository is not connected to Gemini, Groq, FantaLab, Airtable or any external service.
- The examples require **no API keys, accounts or personal documents**.
- No original university survey data or business datasets are supplied.
- Synthetic ML error scores have no bearing on the accuracy of the original academic study.
