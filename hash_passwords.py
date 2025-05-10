# hash_passwords.py

import sys
import os

# Permet à Python de trouver ton dossier "app"
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importe Connexion au lieu de Database
from app.models.user import UserModel

if __name__ == '__main__':
    user_model = UserModel()
    user_model.hash_existing_passwords()
