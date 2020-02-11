from biquery_sql_etl.sources.bigquery import bqc
from biquery_sql_etl.sources.sqldatabase import dbc
from biquery_sql_etl.queries import sql_queries
from loguru import logger


logger.add('logs/queries.log', format="{time} {message}", level="INFO")


def main():
    """Move data between sources."""
    for k, v in sql_queries.items():
        fetched_rows = bqc.fetch_rows(v)
        inserted_rows = dbc.insert_rows(fetched_rows, k, replace=True)
        logger.info(inserted_rows)
