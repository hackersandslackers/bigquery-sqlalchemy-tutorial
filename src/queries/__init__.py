from .read import read_query

prefix = 'src/queries/sql'
analytics_query = read_query(f'{prefix}/analytics.sql')
