# app/routes/auth_routes.py
from flask import render_template, request, redirect, url_for
from app import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logique de connexion ici (vérifier les informations, etc.)
        return redirect(url_for('index'))  # Redirige vers la page d'accueil après la connexion réussie
    return render_template('login.html')  # Affiche le formulaire de connexion


@app.route('/register', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logique de connexion ici (vérifier les informations, etc.)
        return redirect(url_for('index'))  # Redirige vers la page d'accueil après la connexion réussie
    return render_template('register.html')  # Affiche le formulaire de connexion