"""SQL Database Client."""
import logging
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData, Table

logging.basicConfig(filename='logs/sql.log',
                    format='%(asctime)s %(message)s')
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class SQLClient:

    def __init__(self, uri=None, table=None):
        self.uri = uri
        self.table_name = table
        self.engine = create_engine(self.uri)
        self.metadata = MetaData(bind=self.engine)
        self.table = Table(table,
                           self.metadata,
                           autoload=True)

    def insert_rows(self, rows, replace=None):
        """Insert rows into SQL table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {self.table_name}')
        self.engine.execute(self.table.insert(), rows)
        return [row.items()[0][1] for row in rows]

    def fetch_rows(self, query):
        """Fetch rows from SQL table via query."""
        results = self.engine.execute(query).fetchall()
        return results
