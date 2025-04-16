from flask import Flask, render_template

app = Flask(__name__)
def create_app():
    app = Flask(__name__)
    # Configuration et routes ici
    return app

@app.route('/')
def index():
    return render_template("index.html")
