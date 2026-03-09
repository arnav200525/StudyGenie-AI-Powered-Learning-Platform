from flask import Blueprint, render_template, request, redirect, session
import sqlite3 as sq

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sq.connect("users.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (name,email,username,password) VALUES (?,?,?,?)",
            (name,email,username,password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


@auth.route("/login", methods=["GET","POST"])
def login():

    msg=None

    if request.method == "POST":

        username=request.form["username"]
        password=request.form["password"]

        conn=sq.connect("users.db")
        cur=conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username,password)
        )

        user=cur.fetchone()

        cur.execute(
            "SELECT name FROM users WHERE username=?",
            (username,)
        )

        actual_name=cur.fetchone()

        conn.close()

        if actual_name:
            session["name"]=actual_name[0]

        if user:
            return redirect("/welcome")
        else:
            msg="Wrong Password!!"

    return render_template("login.html",message=msg)


@auth.route("/welcome")
def welcome():

    if "name" in session:
        return render_template("welcome.html",uname=session["name"])
    else:
        return redirect("/login")


@auth.route("/logout")
def logout():

    session.pop("name",None)
    return redirect("/login")