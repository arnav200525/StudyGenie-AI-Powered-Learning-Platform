from flask import Blueprint, render_template, session, redirect
import sqlite3 as sq

profile = Blueprint("profile", __name__)

@profile.route("/profile")
def profile1():

    if "name" not in session:
        return redirect("/login")

    conn=sq.connect("users.db")
    cur=conn.cursor()

    cur.execute(
        "SELECT email,username FROM users WHERE name=?",
        (session["name"],)
    )

    result=cur.fetchone()

    conn.close()

    if result:

        email,username=result

        session["email"]=email
        session["username"]=username

    else:
        return "User not found",404

    return render_template(
        "profile.html",
        username=username,
        name=session["name"],
        email=email
    )