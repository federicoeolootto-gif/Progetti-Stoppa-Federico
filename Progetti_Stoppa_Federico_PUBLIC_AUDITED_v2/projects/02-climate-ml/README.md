# Education, Climate Policy & Machine Learning

**Original work:** University of Padua group coursework examining education and climate-related attitudes by combining European survey information and compulsory-schooling reforms. Supplied materials describe OLS, instrumental-variable 2SLS, Double Machine Learning with Random Forest nuisance models, cross-fitting, and decision-tree cost-complexity pruning. Multiple students contributed; no individual authorship of the entire study is claimed here.

**Important qualification:** the presentation reports a test RMSE of 0.187 for a pruned decision tree; original-source reproduction and source-data publication rights have not been independently established. The source notebook also includes outputs and data paths and is NOT uploaded.

## Public code

[`synthetic_ml_demo.py`](synthetic_ml_demo.py) is an **independently written illustration** of a reproducible train/test split, baseline, decision-tree tuning on training folds and out-of-sample comparison with Random Forest. Its generated data, coefficients and RMSE are fictional and **not** the original education/climate estimates. This demo does **not** establish a causal relationship or implement the original IV/DML model.

```bash
pip install -r ../../requirements-demos.txt
python synthetic_ml_demo.py
```
