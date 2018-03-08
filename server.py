"""Zendesk tickets."""

from jinja2 import StrictUndefined

from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

import zendesk_api as zd

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "\x92V\xae\x14\xbfT\xc4\x17\x8f\xd5;\x08"

app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Homepage."""
    return render_template("homepage.html")


@app.route("/", methods=["POST"])
def log_user_in():
    """Uses user auth to get tickets."""
    email = request.form.get("email")
    password = request.form.get("password")
    subdomain = request.form.get("subdomain")

    session["email"] = email
    session["password"] = password
    session["subdomain"] = subdomain
    return redirect("/tickets")


@app.route("/logout")
def log_user_out():
    """Logs out the user."""
    session.clear()
    # session.pop('user')
    flash("Logged out")

    return redirect("/")


@app.route("/tickets")
def ticket_list():
    """Shows the list of tickets."""
    resp = zd.request(zd.format_subdomain(session["subdomain"]), session["email"], session["password"])
    tix = resp["tickets"]
    return render_template("ticket_list.html", tickets=tix)


@app.route("/tickets/<ticket_id>", methods=["GET"])
def ticket_details(ticket_id):
    """Shows a ticket's details."""
    ticket_url = zd.format_ticket(session["subdomain"], ticket_id)
    resp = zd.request(ticket_url, session["email"], session["password"])
    ticket = resp["ticket"]

    return render_template("ticket_details.html", ticket=ticket)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    app.run(port=5000, host='0.0.0.0')
