from os import environ

# Google BigQuery config
gcp_credentials = environ.get('GCP_CREDENTIALS')
gcp_project = environ.get('GCP_PROJECT')
bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
bigquery_table = environ.get('GCP_BIGQUERY_TABLE')

# SQL database config
database_username = environ.get('DATABASE_USERNAME')
database_password = environ.get('DATABASE_PASSWORD')
database_host = environ.get('DATABASE_HOST')
database_port = environ.get('DATABASE_PORT')
database_name = environ.get('DATABASE_DATABASE_NAME')
database_table = environ.get('DATABASE_TABLE_NAME')

# Local
local_sql_folder = 'sql'
