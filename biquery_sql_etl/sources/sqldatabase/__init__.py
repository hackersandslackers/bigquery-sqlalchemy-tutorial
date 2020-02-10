from config import (database_username,
                    database_password,
                    database_host,
                    database_port,
                    database_table,
                    database_name)
from .database_client import Database

dbc = Database('mysql',
               username=database_username,
               password=database_password,
               host=database_host,
               port=database_port,
               db_name=database_name,
               table=database_table)
