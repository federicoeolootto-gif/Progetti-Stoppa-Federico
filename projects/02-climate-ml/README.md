# Education, Climate Attitudes & Machine Learning

**Research question:** Can additional education affect climate-related beliefs, policy preferences and behaviours? How do conventional econometric estimates compare with flexible machine-learning-based methods?

This was **collaborative University of Padua coursework**. The original study combines European survey outcomes with variation from compulsory-schooling legislation. The work included OLS, instrumental-variable 2SLS, Double Machine Learning with Random Forest nuisance models and cost-complexity pruning of decision trees.

## Analytical workflow

1. Merge, clean and check multi-country data, including reform-exposure variables.
2. Contrast associational OLS estimates with IV-based estimates under stated identification assumptions.
3. Investigate covariate balance, model uncertainty and robustness.
4. Explore DML and evaluate predictive models on held-out data.

## What you can inspect

- [Synthetic Python ML example](synthetic_ml_demo.py): reproducible train/test split, mean baseline, cross-validated decision tree and Random Forest.
- [Test suite](../../tests/test_public_portfolio.py) · [Reproduction instructions](../../docs/RUN_DEMOS.md).

**Important distinction:** the public script uses computer-generated data. It does **not** reproduce 2SLS, DML or estimates from the university analysis. An original presentation reported a decision-tree test RMSE of 0.187, but that figure is **not** independently reproduced here and should not be compared to the synthetic demo's metrics.

**Tools & methods in the university work:** Python, pandas, Statsmodels, scikit-learn, DoubleML; causal inference and model validation. Coauthor and data redistribution permissions require further review before original notebooks can be released.
