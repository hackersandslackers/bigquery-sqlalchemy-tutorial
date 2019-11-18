from src.sources.bigquery import bqc
from src.sources.database import dbc
from src.queries import analytics_query


def main():
    """Move data between sources."""
    fetched_rows = bqc.fetch_rows(analytics_query)
    inserted_rows = dbc.insert_rows(fetched_rows, replace=True)
    print(inserted_rows)
