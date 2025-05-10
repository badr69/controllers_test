# app/models/ride.py
from .db import Connexion

class RideModel(Connexion):
    def __init__(self):
        super().__init__()

    def get_all_rides(self):
        conn = self.get_conn()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM rides")
                    return cur.fetchall()
            finally:
                self.put_conn(conn)
        return []
