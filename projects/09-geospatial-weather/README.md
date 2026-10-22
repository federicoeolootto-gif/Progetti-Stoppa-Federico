# Geospatial Aggregation · Python Demonstration

**Problem:** Aggregate nearby geolocated observations without mis-handling missing values, invalid coordinates or distance weights.

Inspired by a previous research-assistant technical exercise, this **independent public example** implements Haversine distance, radius filtering and inverse-distance weighting of fictional observations.

[Source](spatial_weights.py) · [Tests](../../tests/test_public_portfolio.py)

```bash
python projects/09-geospatial-weather/spatial_weights.py
```

Important: this is not the original recruitment dataset or assignment. A weighted mean of rainfall **depth** is not an estimate of total rainfall **volume**; that requires consistent physical units and spatial coverage.
