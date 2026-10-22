# Federico Stoppa · Data Analytics, Business Analysis & Consulting

**Applied Economics (MSc, 110/110 cum laude) · Business Intelligence · Machine Learning · Decision Support**

I work at the intersection of quantitative analysis and practical business problems: organising data, defining useful KPIs, building analytical workflows and turning results into decisions. My background combines a Business Intelligence internship with applied econometrics and personal software projects.

This portfolio is designed to make the work **easy to inspect**: each project explains the problem, method, my contribution and the evidence available. Links marked **synthetic demo** are safe, independently written illustrations—not copies of private source code or production results.

## Start with these projects

| Project | What it demonstrates | Explore |
|---|---|---|
| **Support Operations Analytics** · Business Intelligence | KPI definition, ticket analysis, PostgreSQL queries and reporting logic, informed by a QlikView internship | [Case study](projects/01-support-analytics/README.md) · [Example results](projects/01-support-analytics/SAMPLE_RESULTS.md) · [SQL](projects/01-support-analytics/sql/02_kpis.sql) |
| **Education & Climate Policy** · Machine Learning | Applied research with IV/2SLS, Double Machine Learning, Random Forest and Decision Trees; separate reproducible ML illustration | [Research overview](projects/02-climate-ml/README.md) · [Python demo](projects/02-climate-ml/synthetic_ml_demo.py) |
| **FantaGiungla** · Decision Support | Event-driven analytics, dynamic budgets, data modelling and development of predictive ML | [Architecture & scope](projects/03-fantagiungla/README.md) · [Event-processing demo](projects/03-fantagiungla/public_event_demo.py) |
| **Nova** · AI Integration | Electron/Node.js application integrating LLM APIs, local retrieval and speech-to-text; resilient provider orchestration | [Application overview](projects/04-nova/README.md) · [Offline API-fallback demo](projects/04-nova/mock_provider_demo.cjs) |
| **PaperLens** · Document AI / Infrastructure | Adaptation of an existing open-source research application using Docker, OpenSearch, PostgreSQL and document retrieval | [Technical overview & attribution](projects/05-paperlens/README.md) |

### Selected capabilities

- **Analytics and BI:** QlikView, Excel, Airtable, Python (pandas, NumPy), KPI design, data cleaning and validation.
- **Modelling:** econometrics, causal inference, panel methods, IV/2SLS, DoubleML, scikit-learn, R, Stata and optimization.
- **Software and data systems:** JavaScript, Node.js, Electron, REST/LLM API integrations, Git, Docker Compose, PostgreSQL, Redis and OpenSearch.

These tools were used at different depths across coursework, self-directed projects and employment; listing a tool is not a claim of production expertise. **Power BI Desktop and predictive ML for FantaGiungla are in development**, not completed published deliverables.

## More work

| Theme | Project |
|---|---|
| Economic history & causal inference | [Bourbon Royal Roads and municipal population](projects/06-historical-roads/README.md) |
| Time-series econometrics | [Macroeconomic VAR and impulse responses](projects/07-var/README.md) |
| Corporate finance & strategy | [Pirelli financial reporting and valuation](projects/08-pirelli/README.md) |
| Spatial data workflows | [Geospatial aggregation — runnable Python illustration](projects/09-geospatial-weather/README.md) |
| International research | [University of Bonn research project](projects/10-bonn/README.md) |
| Mathematical modelling | [Mean field games](projects/11-mean-field/README.md) · [Constrained optimization](projects/12-optimization/README.md) |
| Broader experience | [Hackathons, tutoring and communication](projects/13-other/README.md) |

## Try the public demos

All demo records are **fictional**; there are **no credentials, live external APIs or employer data**. Use Python 3.10+ and Node.js 18+.

```bash
python -m pip install -r requirements-demos.txt
python -m unittest discover -s tests -v
node --test projects/04-nova/mock_provider.test.cjs

# Optional: inspect standalone demonstrations
python projects/01-support-analytics/report_demo.py
python projects/02-climate-ml/synthetic_ml_demo.py
python projects/03-fantagiungla/public_event_demo.py
```

See the [reproduction guide](docs/RUN_DEMOS.md) for platform notes and the optional PostgreSQL queries. The portfolio has test code; successful execution on your own machine depends on installing the listed dependencies.

---

**Scope and attribution.** Some original datasets and application sources are not distributed because of privacy, intellectual-property or research-publication constraints. Examples are labelled as such in the individual case studies. See [publication audit](PUBLICATION_AUDIT.md), [security and provenance](SECURITY.md) and [project evidence index](docs/PROJECT_EVIDENCE.md). For the PaperLens third-party foundation, see its [upstream attribution](projects/05-paperlens/README.md).
