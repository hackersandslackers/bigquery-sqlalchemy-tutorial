"""Base Data Client."""
from sqlalchemy import Table


class BaseClient:

    def __init__(self, engine=None, metadata=None, table=None):
        self.engine = engine
        self.metadata = metadata
        self.table = table

    def insert_rows(self, rows, table, replace=None):
        """Insert rows into table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {table}')
        table = Table(table, self.metadata, autoload=True)
        self.engine.execute(table.insert(), rows)
        return self.__construct_response(table, rows)

    def fetch_rows(self, query):
        """Fetch all rows via query."""
        rows = self.engine.execute(query).fetchall()
        return rows

    @staticmethod
    def __construct_response(table, rows):
        """Summarize results of an executed query."""
        columns = rows[0].keys()
        column_names = ", ".join(columns)
        num_rows = len(rows)
        return f'Inserted {num_rows} rows into `{table}` with {len(columns)} columns: {column_names}'
