import logging
from .bigquery_client import BigQueryClient
from .mysql_client import MySQLClient
from config import Config

logging.basicConfig(format='%(asctime)s \n%(message)s', level=logging.INFO)


def main():
    bigquery = BigQueryClient(Config)
    mysql = MySQLClient(Config)
    bq_rows = bigquery.fetch_bigquery_rows()
    updated = mysql.insert_rows(bq_rows)
    logging.info(f'Top posts this week: {updated}')
