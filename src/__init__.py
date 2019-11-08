import logging
from .bigquery import BigQueryClient
from .database import MySQLClient
from config import Config

logging.basicConfig(format='%(asctime)s \n%(message)s',
                    level=logging.INFO)


def main():
    bigquery = BigQueryClient(Config)
    mysql = MySQLClient(Config)
    bq_rows = bigquery.fetch_bigquery_rows(Config.bigquery_query)
    updated = mysql.insert_rows(bq_rows)
    logging.info(f'Top posts this week: {updated}')
