"""Independent, synthetic predictive-model illustration; NOT the source research."""
from __future__ import annotations

import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.tree import DecisionTreeRegressor


def generate_synthetic(n: int = 360, seed: int = 2026):
    """Return purely simulated data with no survey records or causal interpretation."""
    if n < 30:
        raise ValueError("n should be at least 30")
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 78, size=n)
    simulated_education = rng.integers(7, 22, size=n)
    engagement = rng.normal(size=n)
    X = np.column_stack((age, simulated_education, engagement))
    # Arbitrary data-generating function, not a causal model.
    y = 0.05 * simulated_education + 0.12 * np.tanh(engagement) + 0.0008 * (age - 45)**2 + rng.normal(0, 0.15, n)
    return X, y


def evaluate(seed: int = 2026) -> dict[str, float]:
    X, y = generate_synthetic(seed=seed)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed
    )
    cv = KFold(n_splits=5, shuffle=True, random_state=seed)
    tree = GridSearchCV(
        DecisionTreeRegressor(random_state=seed),
        param_grid={"max_depth": [2, 3, 4, 5], "min_samples_leaf": [4, 10, 18]},
        scoring="neg_mean_squared_error", cv=cv, n_jobs=1
    )
    models = {
        "mean_baseline": DummyRegressor(strategy="mean"),
        "decision_tree": tree,
        "random_forest": RandomForestRegressor(
            n_estimators=80, min_samples_leaf=5, random_state=seed, n_jobs=1
        ),
    }
    result = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        result[name] = float(np.sqrt(mean_squared_error(y_test, model.predict(X_test))))
    return result


if __name__ == "__main__":
    print("Synthetic test-set RMSE (lower is better; not real research data)")
    for model, error in evaluate().items():
        print(f"{model}: {error:.4f}")
