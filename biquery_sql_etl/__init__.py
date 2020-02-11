from loguru import logger
from biquery_sql_etl.engines import bigquery_engine, rdbms_engine
from biquery_sql_etl.queries import sql_queries
from biquery_sql_etl.client import DataClient
from config import bigquery_table


logger.add('logs/queries.log', format="{time} {message}", level="INFO")


def init_pipeline():
    """Move data between Bigquery and MySQL."""
    total_rows_affected = 0
    bqc, dbc = data_sources()
    for table_name, query in sql_queries.items():
        fetched_rows = bqc.fetch_rows(query, table=bigquery_table)
        inserted_rows = dbc.insert_rows(fetched_rows, table_name, replace=True)
        logger.info(inserted_rows)
        total_rows_affected += len(fetched_rows)
    logger.info(f"Completed migration of {total_rows_affected} rows from BigQuery to MySQL.")


def data_sources():
    """Construct datasources."""
    bqc = DataClient(bigquery_engine)
    dbc = DataClient(rdbms_engine)
    return bqc, dbc
