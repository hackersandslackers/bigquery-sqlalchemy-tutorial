"""BigQuery data source."""
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData


class BigQueryClient:

    def __init__(self, Config):
        self.metadata = MetaData()
        self.uri = Config.bigquery_uri
        self.credentials = Config.gcp_credentials
        self.query = Config.bigquery_query
        self.engine = create_engine(self.uri,
                                    credentials_path=self.credentials)

    def fetch_bigquery_rows(self):
        """Fetch rows from BigQuery via query."""
        results = self.engine.execute(self.query).fetchall()
        return results
