# Support Operations Analytics · BI Case Study

**Question:** How can a support team understand workload, response times and unresolved cases without misleading KPI definitions?

During a Data Analyst internship, I worked with Business Intelligence reporting, QlikView, KPI monitoring and data-quality checks. This public **independent demonstration** applies comparable analytical reasoning to an entirely fictional ticket dataset; it is not a reproduction of employer dashboards or customer records.

## Approach

1. Define business terms: *tickets opened*, *closed cases*, *observed first view*, *case resolution time* and *assignments*.
2. Design a small relational-friendly ticket schema and inspect missing/invalid timestamps.
3. Aggregate outcomes by team and time, without treating unresolved cases as zero-hour resolutions.
4. Present summary results and a Power BI Desktop build guide (no completed `.pbix` published).

## Inspectable evidence

- [Synthetic CSV — 60 records](data/support_tickets_synthetic.csv) · [Schema](sql/01_schema.sql) · [PostgreSQL KPI queries](sql/02_kpis.sql)
- [Python reporting script](report_demo.py) · [Calculated sample results](SAMPLE_RESULTS.md)
- [Dashboard design notes](dashboard_guide.md) · [Run guide](../../docs/RUN_DEMOS.md)

**Methods & tools:** QlikView (internship); Python, SQL/PostgreSQL, CSV, KPI definitions and Power BI design (public demonstrator).

**Boundary:** No actual Best Tool records, QlikView documents, customers, company charts or proprietary formulae are included. The test data do not establish business impact at an employer.
