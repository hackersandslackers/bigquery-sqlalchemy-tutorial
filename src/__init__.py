from config import Config
from src.bigquery import BigQueryClient
from src.database import SQLClient
from src.util.read import get_query_from_file


def main():
    bigquery = init_bigquery()
    database = init_database()
    query = get_query_from_file(Config.bigquery_query)
    rows = bigquery.fetch_rows(query)
    updated = database.insert_rows(rows, replace=True)
    print(updated)


def init_bigquery():
    """Initiate BigQuery Client."""
    uri, creds = Config.get_bigquery_config()
    bigquery = BigQueryClient(uri=uri, creds=creds)
    return bigquery


def init_database():
    """Initiate SQL database Client."""
    uri, table = Config.get_database_config(type='mysql')
    bigquery = SQLClient(uri=uri, table=table)
    return bigquery
