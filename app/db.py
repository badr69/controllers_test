import psycopg2
from app import Config


def get_connection():
    conn = psycopg2.connect(Config)
    return conn

    with open('schema.sql', 'r') as file:
            schema_sql = file.read()