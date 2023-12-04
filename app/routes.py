from functools import wraps

import werkzeug
from flask import flash, redirect, render_template, request, url_for

from app import app
from app.connection import get_db_connection
from app.forms import ConnectionForm, DisconnectionForm
from app.models import User


def connection_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = User()
        if not user.authenticated:
            return redirect(url_for("connection", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/connection", methods=["GET", "POST"])
def connection():
    user = User()
    if user.authenticated:
        flash("User {} already connected".format(user.username))
        return redirect(url_for("index"))
    form = ConnectionForm()
    if form.validate_on_submit():
        flash("Connection to database for user {}".format(form.username.data))
        User(form)
        next_page = request.args.get("next")
        if not next_page:
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("connection.html", title="Sign In", form=form)


@app.route("/disconnection", methods=["GET", "POST"])
def disconnection():
    form = DisconnectionForm()
    if form.validate_on_submit():
        user = User()
        setattr(user, "authenticated", False)
        user.set_vars()
        flash("Disconnected user {}".format(user.username))
        return redirect(url_for("index"))
    return render_template("disconnection.html", title="Disconnect", form=form)


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Kelly"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool."},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
