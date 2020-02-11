"""SQL Database Engine."""

from sqlalchemy.engine import create_engine
from config import (gcp_credentials,
                    bigquery_uri)


bigquery_engine = create_engine(bigquery_uri, credentials_path=gcp_credentials)
