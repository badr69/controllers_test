from flask import request, render_template, redirect, session
from app.models.user import User

def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.authenticate(email, password)
        if user:
            session["user_id"] = user.id
            return redirect("/rides")
        else:
            return "Email ou mot de passe incorrect"
    return render_template("login.html")

def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        User.create(username, email, password)
        return redirect("/login")
    return render_template("register.html")