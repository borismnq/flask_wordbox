import configparser
import os

class ConfigDatabase:
    db_info = configparser.ConfigParser()
    db_info.read('app/database/database.ini')
    postgres_access = {value[0]: value[1] for value in db_info.items('POSTGRES_CONNECT')}
    if new_value := os.environ.get('DATABASE_HOST'):
        postgres_access['host'] = new_value
    if new_value := os.environ.get('DATABASE_PASSWORD'):
        postgres_access['password'] = new_value
    if new_value := os.environ.get('DATABASE_DATABASE'):
        postgres_access['database'] = new_value
    if new_value := os.environ.get('DATABASE_USER'):
        postgres_access['user'] = new_value
    table_name = db_info.get('USERS_TABLE', 'table_name')
    (postgres_access)