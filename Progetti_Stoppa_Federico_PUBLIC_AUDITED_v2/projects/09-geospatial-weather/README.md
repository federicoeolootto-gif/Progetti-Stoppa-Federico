# Geospatial Aggregation — Synthetic Python Demo

A former research-assistant technical exercise motivated this **independent fictional illustration** of distance-weighted aggregation. Neither the original task instructions nor its rainfall/weather data are reproduced.

`spatial_weights.py` computes great-circle Haversine distances, filters observations within a configurable radius, skips missing values and uses inverse-square-distance weights. It handles exact coordinate matches and raises errors for invalid coordinates/non-finite values.

```bash
python spatial_weights.py
python -m unittest discover -s ../../tests -v
```

The demo's geographic points and measurements are fictional. An IDW mean of precipitation *depth* is **not** total rainfall volume; volume estimation requires consistent physical units and spatial cell areas. The algorithm does not prove equivalence to the full original data task.
