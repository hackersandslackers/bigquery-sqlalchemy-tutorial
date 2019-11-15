"""Read SQL queries from local files."""


def read_query(path):
    """Read contents of file."""
    file = open(path, 'r')
    query = file.read()
    file.close()
    return query
