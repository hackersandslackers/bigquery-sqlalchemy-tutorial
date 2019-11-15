from os import environ


# SQL database config
database_username = environ.get('DATABASE_USERNAME')
database_password = environ.get('DATABASE_PASSWORD')
database_host = environ.get('DATABASE_HOST')
database_port = environ.get('DATABASE_PORT')
database_name = environ.get('DATABASE_DATABASE_NAME')
database_table = environ.get('DATABASE_TABLE_NAME')
