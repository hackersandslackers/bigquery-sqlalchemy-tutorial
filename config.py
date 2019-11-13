"""BigQuery & SQL Configuration."""
from os import environ


class Config:

    # Google Cloud
    gcp_credentials = environ.get('GCP_CREDENTIALS')
    gcp_project = environ.get('GCP_PROJECT')

    # Google BigQuery
    bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
    bigquery_table = environ.get('GCP_BIGQUERY_TABLE')
    bigquery_query = 'queries/analytics.sql'

    # SQL
    database_username = environ.get('DATABASE_USERNAME')
    database_password = environ.get('DATABASE_PASSWORD')
    database_host = environ.get('DATABASE_HOST')
    database_port = environ.get('DATABASE_PORT')
    database_db = environ.get('DATABASE_DATABASE_NAME')
    database_table = environ.get('DATABASE_TABLE_NAME')

    @classmethod
    def get_bigquery_config(cls):
        bigquery_uri = f'bigquery://{cls.gcp_project}/{cls.bigquery_dataset}'
        return bigquery_uri, cls.gcp_credentials

    @classmethod
    def get_database_config(cls, type=None):
        database_flavor = None
        if type.lower() == 'mysql':
            database_flavor = 'mysql+pymysql'
        if type.lower() == 'postgres':
            database_flavor = 'postgresql+psycopg2'
        database_uri = f'{database_flavor}://{cls.database_username}:{cls.database_password}@{cls.database_host}:{cls.database_port}/{cls.database_db}'
        return database_uri, cls.database_table
