"""Application entry point."""
from biquery_sql_etl import init_pipeline

pipeline = init_pipeline()

if __name__ == '__main__':
    pipeline
