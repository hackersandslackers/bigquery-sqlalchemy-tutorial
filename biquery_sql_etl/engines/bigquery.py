from sqlalchemy.engine import create_engine
from config import (gcp_credentials,
                    bigquery_uri)


def create_bigquery_engine(uri, creds):
    engine = create_engine(uri, credentials_path=creds)
    return engine


bigquery_engine = create_bigquery_engine(bigquery_uri, gcp_credentials)
