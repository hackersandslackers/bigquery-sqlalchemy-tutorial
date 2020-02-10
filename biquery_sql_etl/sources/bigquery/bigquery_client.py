"""BigQuery Client."""
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData
from biquery_sql_etl.sources.client import BaseClient


class BigQueryClient(BaseClient):

    def __init__(self, project=None, dataset=None, creds=None, table=None):
        self.uri = f'bigquery://{project}/{dataset}'
        self.engine = create_engine(self.uri, credentials_path=creds)
        super().__init__(engine=self.engine,
                         metadata=MetaData(bind=self.engine),
                         table=table)
