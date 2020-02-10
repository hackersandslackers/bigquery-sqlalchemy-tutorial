"""Read SQL queries from local files."""
from os import listdir
from os.path import isfile, join
from config import local_sql_folder


def get_local_sql_files():
    """Fetch all SQL query files in folder."""
    files = [local_sql_folder + '/' + f for f in listdir(local_sql_folder) if isfile(join(local_sql_folder, f)) if '.sql' in f]
    return files


def read_sql_queries():
    """Read SQL query from .sql file."""
    files = get_local_sql_files()
    file_contents = []
    for file in files:
        fd = open(file, 'r')
        query = fd.read()
        file_contents.append(query)
        fd.close()
    return file_contents


def create_query_dict():
    """Create dictionary of queries for logging purposes."""
    file_names = listdir(local_sql_folder)
    file_contents = read_sql_queries()
    table_names = get_table_name(file_names)
    files = dict(zip(table_names, file_contents))
    return files


def get_table_name(file_names):
    """Assume that table names of queries are [FILE_NAME]_stats."""
    tables = [f"{file.split('.')[0]}_stats" for file in file_names]
    return tables


sql_queries = create_query_dict()
