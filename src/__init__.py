from src.sources.bigquery import bqc
from src.sources.database import dbc
from src.queries import queries


def main():
    """Move data between sources."""
    for k, v in queries.items():
        fetched_rows = bqc.fetch_rows(v)
        inserted_rows = dbc.insert_rows(fetched_rows, k, replace=True)
        print(inserted_rows)
