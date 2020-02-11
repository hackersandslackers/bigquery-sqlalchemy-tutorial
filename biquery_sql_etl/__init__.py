from biquery_sql_etl.engines import bigquery_engine, rdbms_engine
from biquery_sql_etl.queries import sql_queries
from biquery_sql_etl.client import DataClient
from loguru import logger
from config import bigquery_table


logger.add('logs/queries.log', format="{time} {message}", level="INFO")


def main():
    """Move data between sources."""
    bqc = DataClient(bigquery_engine)
    dbc = DataClient(rdbms_engine)
    for table_name, query in sql_queries.items():
        fetched_rows = bqc.fetch_rows(query, table=bigquery_table)
        inserted_rows = dbc.insert_rows(fetched_rows, table_name, replace=True)
        logger.info(inserted_rows)
