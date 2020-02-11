"""SQL Database Client."""
from sqlalchemy.engine import create_engine
from config import rdbms_uri


def create_rdbms_engine(uri):
    return create_engine(uri)


rdbms_engine = create_rdbms_engine(rdbms_uri)
