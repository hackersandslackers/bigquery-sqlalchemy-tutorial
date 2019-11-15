"""SQL Database Client."""
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData
from src.sources.client import BaseClient


class Database(BaseClient):

    def __init__(self,
                 type,
                 username=None,
                 password=None,
                 host=None,
                 port=None,
                 table=None,
                 db_name=None):
        self.table = table
        self.type = self.__conection_type(type)
        self.engine = create_engine(f'{self.type}://{username}:{password}@{host}:{port}/{db_name}')
        super().__init__(engine=self.engine,
                         metadata=MetaData(bind=self.engine),
                         table=table)

    @staticmethod
    def __conection_type(type):
        if type.lower() == 'mysql':
            return 'mysql+pymysql'
        if type.lower() == 'postgres':
            return 'postgresql+psycopg2'
        return None
