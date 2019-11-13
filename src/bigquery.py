"""BigQuery Client."""
import logging
from sqlalchemy.engine import create_engine


logging.basicConfig(filename='logs/bigquery.log',
                    format='%(asctime)s %(message)s')
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class BigQueryClient:

    def __init__(self, uri=None, table=None, creds=None):
        self.uri = uri
        self.table_name = table
        self.creds = creds
        self.engine = create_engine(self.uri,
                                    credentials_path=self.creds)

    def insert_rows(self, rows, replace=None):
        """Insert rows into SQL table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {self.table_name}')
        self.engine.execute(self.table.insert(), rows)
        return [row.items()[0][1] for row in rows]

    def fetch_rows(self, query):
        """Fetch rows from BigQuery via query."""
        results = self.engine.execute(query).fetchall()
        return results
