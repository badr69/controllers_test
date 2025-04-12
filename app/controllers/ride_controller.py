from flask import request, render_template, redirect, session
from app.models.ride import Ride

def list_rides():
    rides = Ride.all()
    return render_template("rides.html", rides=rides)

def add_ride():
    if request.method == "POST":
        Ride.create(
            request.form["departure"],
            request.form["destination"],
            request.form["date"],
            int(request.form["seats"]),
            int(session["user_id"])
        )
        return redirect("/rides")
    return render_template("add_ride.html")