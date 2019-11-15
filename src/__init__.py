from src.sources.bigquery import bqc
from src.sources.database import dbc
from src.queries import analytics_query


def main():
    rows = bqc.fetch_rows(analytics_query)
    updated = dbc.insert_rows(rows, replace=True)
    print(updated)
