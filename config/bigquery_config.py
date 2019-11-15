from os import environ

# Google Cloud config
gcp_credentials = environ.get('GCP_CREDENTIALS')
gcp_project = environ.get('GCP_PROJECT')

# Google BigQuery config
bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
bigquery_table = environ.get('GCP_BIGQUERY_TABLE')
