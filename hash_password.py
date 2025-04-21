# hash_passwords.py

from app.models.user import UserModel

if __name__ == '__main__':
    user_model = UserModel()
    user_model.hash_existing_passwords()
