"""Independent synthetic Haversine / inverse-distance weighting example."""
from __future__ import annotations
import math

EARTH_RADIUS_KM = 6371.0088


def _valid_coordinates(lat, lon) -> bool:
    return (isinstance(lat, (int, float)) and isinstance(lon, (int, float))
            and math.isfinite(lat) and math.isfinite(lon)
            and -90 <= lat <= 90 and -180 <= lon <= 180)


def haversine_km(lat1, lon1, lat2, lon2):
    if not _valid_coordinates(lat1, lon1) or not _valid_coordinates(lat2, lon2):
        raise ValueError("Coordinates must be finite valid latitude/longitude pairs")
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dlat, dlon = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(p1) * math.cos(p2) * math.sin(dlon / 2)**2
    return 2 * EARTH_RADIUS_KM * math.asin(min(1.0, math.sqrt(max(0.0, a))))


def weighted_mean(centroid, observations, radius_km=100.0):
    """Inverse-square-distance mean of (lat, lon, finite_value_or_None)."""
    if not isinstance(radius_km, (int, float)) or not math.isfinite(radius_km) or radius_km <= 0:
        raise ValueError("radius_km must be finite and > 0")
    if len(centroid) != 2 or not _valid_coordinates(*centroid):
        raise ValueError("Invalid centroid")
    valid = []
    for lat, lon, value in observations:
        if value is None:
            continue
        d = haversine_km(*centroid, lat, lon)
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Measurement must be finite numeric or None")
        if d <= radius_km:
            valid.append((d, float(value)))
    if not valid:
        return None
    coincident = [v for d, v in valid if d < 1e-9]
    if coincident:
        return sum(coincident) / len(coincident)
    weights = [1 / (d*d) for d, _ in valid]
    return sum(w*v for w, (_, v) in zip(weights, valid)) / sum(weights)


if __name__ == '__main__':
    examples = [(10.01, 12.00, 12.0), (10.05, 12.05, 21.0), (60.0, 60.0, 8.0)]
    result = weighted_mean((10.0, 12.0), examples)
    print(f"Fictional weighted measurement: {result:.3f}")
