from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.controllers.user_controller import user_controller
from app import user_bp

from app.models import user
from app.models.user import UserModel

app = Flask(__name__)
app.secret_key = "un_truc_bien_secret_que_personne_ne_devine"  # Change ça en production !

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'

    app.register_blueprint(user_bp)

    return app

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user_model = UserModel()
        user_model.create_user(username, email, password)

        flash("Inscription réussie ! Connecte-toi.")
        return redirect(url_for("login"))  # 🔁 redirection vers la route `login`

    return render_template("register.html", error="Tous les champs sont obligatoires.")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Récupérer l'utilisateur depuis la base de données (adapté à ton modèle)
        user_model = UserModel()
        user = user_model.find_by_email(email)  # Supposons que tu aies une méthode pour récupérer l'utilisateur
        # print("DEBUG USER:", user)
        # print("DEBUG - email envoyé :", email)
        # print("DEBUG - mot de passe envoyé :", password)
        # print("DEBUG - mot de passe haché en base :", user["password"])
        # print("DEBUG - Résultat check :", check_password_hash(user["password"], password))

        if user and check_password_hash(user["password"], password):  # Comparaison avec le mot de passe haché
            session["user_id"] = user["id"]  # Enregistrer l'ID de l'utilisateur dans la session
            session["username"] = user["username"]
            flash("Connecté avec succès")
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Identifiants incorrects", "error")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/user_dashboard")
def user_dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    username = session.get("username", "Utilisateur")
    return render_template("user_dashboard.html", username=username)

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/users")
def users():
    users = user_controller.get_all_users()
    print("DEBUG - users :", users)  # ← Ajoute ce print pour debug
    return render_template("users.html", users=users)

@app.route("/logout")
def logout():
    session.pop('user_id', None)  # Supprimer l'ID de l'utilisateur de la session
    return redirect(url_for('login'))  # Redirige vers la page de login après la déconnexion

if __name__ == "__main__":
    app.run(debug=True)











