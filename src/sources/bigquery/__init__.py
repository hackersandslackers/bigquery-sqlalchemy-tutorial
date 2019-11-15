from config.bigquery_config import (gcp_credentials,
                                    gcp_project,
                                    bigquery_dataset,
                                    bigquery_table)
from .bigquery_client import BigQueryClient

bqc = BigQueryClient(project=gcp_project,
                     dataset=bigquery_dataset,
                     table=bigquery_table,
                     creds=gcp_credentials)
