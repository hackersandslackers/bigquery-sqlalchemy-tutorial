from loguru import logger
from biquery_sql_etl.engines import bigquery_engine, rdbms_engine
from biquery_sql_etl.queries import sql_queries
from biquery_sql_etl.client import DataClient


logger.add('logs/queries.log', format="{time} {message}", level="INFO")


def init_pipeline():
    """Move data between Bigquery and MySQL."""
    num_rows = 0
    bqc = DataClient(bigquery_engine)
    dbc = DataClient(rdbms_engine)
    for table_name, query in sql_queries.items():
        rows = bqc.fetch_rows(query)
        insert = dbc.insert_rows(rows, table_name, replace=True)
        logger.info(insert)
        num_rows += len(rows)
    logger.info(f"Completed migration of {num_rows} rows from BigQuery to MySQL.")
