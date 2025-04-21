# app/controllers/user_controller.py

from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash
from app.models.user import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')

            if not name or not email or not password:
                return render_template('register.html', error="Tous les champs sont obligatoires.")

            hashed_password = generate_password_hash(password)
            self.user_model.create_user(name, email, hashed_password)

            return redirect(url_for('login'))

        return render_template('register.html')

    def get_all_users(self):
        users = self.user_model.get_all_users()
        print("DEBUG - Utilisateurs récupérés:", users)
        return [dict(user) for user in users]

# ✅ Création de l'instance à la fin, après la classe
user_controller = UserController()
