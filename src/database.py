"""MySQL data destination."""
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String


class MySQLClient:

    def __init__(self, Config):
        self.mysql_uri = Config.mysql_uri
        self.engine = create_engine(self.mysql_uri)
        self.metadata = MetaData()
        self.table_name = Config.mysql_table
        self.table = Table(Config.mysql_table, self.metadata,
                           Column('id', Integer),
                           Column('title', String),
                           Column('url', String),
                           Column('slug', String),
                           Column('views', Integer))

    def insert_rows(self, rows):
        """Insert rows into MySQL table."""
        self.engine.execute(f'TRUNCATE TABLE {self.table_name}')
        self.engine.execute(self.table.insert(), rows)
        return [row.items()[0][1] for row in rows]
