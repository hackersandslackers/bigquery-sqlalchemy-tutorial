"""Read SQL queries from local files."""


def get_query_from_file(path):
    """Read contents of file."""
    file = open(path, 'r')
    query = file.read()
    file.close()
    return query
