# Applied Analytics · Business Analysis · Consulting

**Public, security-reviewed portfolio** documenting business intelligence, causal inference, machine learning, data integrations and decision-support systems. Entries clearly distinguish a completed group course project, an individual application, an upstream open-source adaptation, and a new **synthetic portfolio demonstration**.

**Public code is NOT a verbatim dump of the original projects.** Source archives were excluded for privacy, licensing, and provenance reasons. The sample implementations are independently written, publicly reproducible demonstrations of selected techniques, with fictional data. Actual application code can only be released after a full source-by-source rights and security review.

## Featured projects

| Project | Focus | Public evidence and limitations |
|---|---|---|
| [Support Operations Analytics](projects/01-support-analytics/README.md) | QlikView, KPI analysis, business intelligence | Internship experience plus **fictional** PostgreSQL dataset and SQL queries; no employer files |
| [Education & Climate Policy](projects/02-climate-ml/README.md) | Python, causal inference, machine learning | Collaborative coursework; offline [synthetic ML illustration](projects/02-climate-ml/synthetic_ml_demo.py), not original research estimates |
| [FantaGiungla](projects/03-fantagiungla/README.md) | Airtable, event streams, budget optimization | Individual, still in development; [synthetic event-processing demonstration](projects/03-fantagiungla/public_event_demo.py) |
| [Nova Desktop AI](projects/04-nova/README.md) | Electron, Node.js, document retrieval and LLM APIs | Individual application; [offline mocked-provider fallback demonstration](projects/04-nova/mock_provider_demo.cjs), not the production client |
| [PaperLens Extension](projects/05-paperlens/README.md) | Docker, PostgreSQL, Redis, OpenSearch, retrieval | Adaptation of an [existing MIT-licensed project](https://github.com/hridaya14/PaperLens); original code not redistributed |

## Additional case studies

- [Bourbon Roads and Municipal Population](projects/06-historical-roads/README.md): spatial data, fixed effects and event-study econometrics; original research materials withheld pending publication coordination.
- [Macroeconomic VAR and Impulse Responses](projects/07-var/README.md): academic time-series modelling; no unsupported performance claims.
- [Pirelli Financial Analysis](projects/08-pirelli/README.md): collaborative accounting and valuation case study; licensed data not redistributed.
- [Geospatial Aggregation](projects/09-geospatial-weather/README.md): **fictional, runnable** Python distance-weighting micro-demo.
- [University of Bonn Research](projects/10-bonn/README.md): original academic IV/2SLS project; restricted source microdata excluded.
- [Mean Field Games](projects/11-mean-field/README.md): undergraduate mathematical modelling and Python simulations.
- [Nonlinear Optimization](projects/12-optimization/README.md): collaborative KKT coursework; not health guidance.
- [Other Activities](projects/13-other/README.md): selected hackathons, tutoring and creative activities.

## Tooling and methodological exposure

Python, R, JavaScript, SQL (demonstration), Excel, QlikView, pandas, NumPy, scikit-learn, Statsmodels, DoubleML, Stata, Airtable, Node.js, Electron, REST/LLM APIs, Docker Compose, PostgreSQL, Redis, OpenSearch, Jupyter, Git/GitHub; econometrics, optimization and spatial analysis. Technologies were used at different depths across different projects. No professional proficiency levels are implied.

**In progress, not a completed deliverable:** FantaGiungla predictive ML and an independent Power BI Desktop report.

## Run the public demonstrations

Requirements: Python 3.10+; Node.js 18+ for the Nova mock; `pip install -r requirements-demos.txt` for the ML demonstration. PostgreSQL is optional and is only needed to execute the native SQL scripts.

```bash
python -m unittest discover -s tests -v
python projects/02-climate-ml/synthetic_ml_demo.py
python projects/03-fantagiungla/public_event_demo.py
python projects/09-geospatial-weather/spatial_weights.py
node --test projects/04-nova/mock_provider.test.cjs
```

The Python tests do not require access to external accounts, live APIs, employer data, or third-party databases. See [Security and Attribution](SECURITY.md) and [Audit Notes](PUBLICATION_AUDIT.md).
