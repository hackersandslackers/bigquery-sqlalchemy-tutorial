from os import environ

# Google BigQuery config
gcp_credentials = environ.get('GCP_CREDENTIALS')
gcp_project = environ.get('GCP_PROJECT')
bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
bigquery_table = environ.get('GCP_BIGQUERY_TABLE')
bigquery_uri = f'bigquery://{gcp_project}/{bigquery_dataset}'

# SQL database config
rdbms_user = environ.get('DATABASE_USERNAME')
rdbms_pass = environ.get('DATABASE_PASSWORD')
rdbms_host = environ.get('DATABASE_HOST')
rdbms_port = environ.get('DATABASE_PORT')
rdbms_name = environ.get('DATABASE_NAME')
rdbms_uri = f'mysql+pymysql://{rdbms_user}:{rdbms_pass}@{rdbms_host}:{rdbms_port}/{rdbms_name}'

# Local
local_sql_folder = 'sql'
