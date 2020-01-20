from .read import read_query

prefix = 'src/queries/sql'

queries = {'weekly_stats': read_query(f'{prefix}/weekly.sql'),
           'monthly_stats': read_query(f'{prefix}/monthly.sql')}
