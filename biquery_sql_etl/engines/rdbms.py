"""SQL Database Engine."""
from sqlalchemy.engine import create_engine
from config import rdbms_uri


rdbms_engine = create_engine(rdbms_uri)
