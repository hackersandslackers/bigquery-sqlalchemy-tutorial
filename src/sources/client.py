"""Base Data Client."""
import logging
from sqlalchemy import Table


logging.basicConfig(filename='logs/queries.log',
                    format='%(asctime)s %(message)s')
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class BaseClient:

    def __init__(self, engine=None, metadata=None, table=None):
        self.table = table
        self.engine = engine
        self.metadata = metadata

    def insert_rows(self, rows, replace=None):
        """Insert rows into table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {self.table}')
        table = Table(self.table, self.metadata, autoload=True)
        self.engine.execute(table.insert(), rows)
        return self.__construct_response(rows)

    def fetch_rows(self, query):
        """Fetch all rows via query."""
        rows = self.engine.execute(query).fetchall()
        return rows

    def __construct_response(self, rows):
        """Summarize results of an executed query."""
        columns = rows[0].keys()
        column_names = ", ".join(columns)
        num_rows = len(rows)
        return f'Inserted {num_rows} rows into `{self.table}` with {len(columns)} columns: {column_names}'
