# app/models/user.py
from werkzeug.security import generate_password_hash, check_password_hash


from .db import Connexion

class UserModel(Connexion):
    def __init__(self):
        super().__init__()

    def find_by_email(self, email):
        conn = self.get_conn()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                    return cur.fetchone()
            finally:
                self.put_conn(conn)
        return None

    def create_user(self, username, email, password):
        conn = self.get_conn()
        if conn:
            try:
                email = email.strip().lower()
                hashed_password = generate_password_hash(password)
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                        (username, email, hashed_password)
                    )
                    conn.commit()
                    print(f"Utilisateur {username} créé avec succès.")
            except Exception as e:
                conn.rollback()
                print(f"Erreur lors de la création de l'utilisateur : {e}")

            finally:
                self.put_conn(conn)

    def verify_user(self, email, password):
        conn = self.get_conn()
        if conn:
            try:
                email = email.strip().lower()
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                    user = cur.fetchone()
                    if user:
                        stored_hashed_password = user[3] # ⚠️ adapte si l’index est différent
                        if check_password_hash(stored_hashed_password, password):
                            print("Authentification réussie.")
                            return user  # ou juste True
            finally:
                self.put_conn(conn)
        return None  # ou False

    def hash_existing_passwords(self):
        conn = self.get_conn()
        if conn:
            try:
                with conn.cursor() as cur:
                    # Sélectionne tous les utilisateurs
                    cur.execute("SELECT id, password FROM users")
                    users = cur.fetchall()

                    for user in users:
                        user_id = user[0]  # Récupérer l'ID de l'utilisateur (généralement dans la première colonne)
                        password = user[3]  # Mot de passe en clair ou haché

                        # Si le mot de passe n'est pas déjà haché (commence par "pbkdf2:" ou "scrypt:")
                        if password and not (password.startswith("pbkdf2:") or password.startswith("scrypt:")):
                            print(f"DEBUG: user_id={user_id}, password={password} (en clair)")

                            # Si en clair, on le hache
                            hashed = generate_password_hash(password)

                            cur.execute(
                                "UPDATE users SET password = %s WHERE id = %s",
                                (hashed, user_id)
                            )
                            print(f"Mot de passe de l'utilisateur {user_id} mis à jour.")

                    conn.commit()

            except Exception as e:
                conn.rollback()
                print(f"Erreur lors du hachage des mots de passe : {e}")
            finally:
                self.put_conn(conn)

    def get_all_users(self):
        conn = self.get_conn()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users")
                    users = cur.fetchall()  # Récupère tous les utilisateurs
                    print("DEBUG - Utilisateurs récupérés:", users)  # Ajout du message de débogage
                    return users
            except Exception as e:
                print(f"DEBUG - Erreur lors de la récupération des utilisateurs : {e}")
            finally:
                self.put_conn(conn)
        else:
            print("DEBUG - Connexion à la base de données échouée")
        return []


