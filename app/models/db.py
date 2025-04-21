# app/models/db.py
import os
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

class Connexion:
    _pool = None

    def __init__(self):
        if Connexion._pool is None:
            Connexion._pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                user=os.getenv("DB_USER", "badr"),
                password=os.getenv("DB_PASSWORD", "Setif_19000"),
                host=os.getenv("DB_HOST", "postgresql-badr.alwaysdata.net"),
                port=os.getenv("DB_PORT", "5432"),
                database=os.getenv("DB_NAME", "badr_ecobusdb"),
                cursor_factory=RealDictCursor
            )

    def get_conn(self):
        try:
            return Connexion._pool.getconn()
        except Exception as e:
            print(f"[ERREUR] Connexion : {e}")
            return None

    def put_conn(self, conn):
        try:
            Connexion._pool.putconn(conn)
        except Exception as e:
            print(f"[ERREUR] Remise au pool : {e}")

    @classmethod
    def close_all_connections(cls):
        if cls._pool:
            cls._pool.closeall()
