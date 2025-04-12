from config import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @staticmethod
    def create(username, email, password):
        conn = get_connection()
        cur = conn.cursor()
        hashed = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, hashed))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def authenticate(email, password):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, username, email, password FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row and check_password_hash(row[3], password):
            return User(row[0], row[1], row[2])
        return None