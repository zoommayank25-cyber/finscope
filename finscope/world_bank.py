"""Small client for the World Bank Indicators API."""
from __future__ import annotations

import pandas as pd
import requests

BASE_URL = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"


def fetch_indicator(country: str, indicator: str, start_year: int, end_year: int) -> pd.DataFrame:
    """Fetch annual indicator observations and return year/value columns."""
    if start_year > end_year:
        raise ValueError("start_year must be less than or equal to end_year.")
    url = BASE_URL.format(country=country, indicator=indicator)
    response = requests.get(
        url,
        params={"format": "json", "date": f"{start_year}:{end_year}", "per_page": 2000},
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list) or len(payload) < 2 or not payload[1]:
        return pd.DataFrame(columns=["year", "value"])
    rows = [
        {"year": int(item["date"]), "value": item["value"]}
        for item in payload[1]
        if item.get("value") is not None
    ]
    return pd.DataFrame(rows, columns=["year", "value"]).sort_values("year")
