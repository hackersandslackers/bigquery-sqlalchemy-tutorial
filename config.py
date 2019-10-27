"""BigQuery & SQL Configuration."""
from os import environ


class Config:

    # Google Cloud
    gcp_credentials = environ.get('GCP_CREDENTIALS')
    gcp_project = environ.get('GCP_PROJECT')

    # Google BigQuery
    bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
    bigquery_table = environ.get('GCP_BIGQUERY_TABLE')
    bigquery_uri = f'bigquery://{gcp_project}/{bigquery_dataset}'
    bigquery_query = environ.get('GCP_BIGQUERY_QUERY')

    # MySQL
    mysql_username = environ.get('MYSQL_USERNAME')
    mysql_password = environ.get('MYSQL_PASSWORD')
    mysql_host = environ.get('MYSQL_HOST')
    mysql_port = environ.get('MYSQL_PORT')
    mysql_db = environ.get('MYSQL_DATABASE_NAME')
    mysql_table = environ.get('MYSQL_TABLE_NAME')
    mysql_uri = f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_db}'
