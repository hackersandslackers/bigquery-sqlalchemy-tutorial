"""SQL Database Client."""
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData
from biquery_sql_etl.sources.client import BaseClient


class Database(BaseClient):

    def __init__(self,
                 db_type,
                 username=None,
                 password=None,
                 host=None,
                 port=None,
                 table=None,
                 db_name=None):
        self.table = table
        self.type = self.__connection_type(db_type)
        self.engine = create_engine(f'{self.type}://{username}:{password}@{host}:{port}/{db_name}')
        super().__init__(engine=self.engine,
                         metadata=MetaData(bind=self.engine),
                         table=table)

    @staticmethod
    def __connection_type(db_type):
        if db_type.lower() == 'mysql':
            return 'mysql+pymysql'
        if db_type.lower() == 'postgres':
            return 'postgresql+psycopg2'
        return None
