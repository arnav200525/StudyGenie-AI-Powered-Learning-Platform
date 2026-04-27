from flask import Blueprint, render_template, session, redirect
import sqlite3 as sq

profile = Blueprint("profile", __name__)

@profile.route("/profile")
def profile1():

    if "user_id" not in session:
        return redirect("/login")

    conn=sq.connect("users.db")
    cur=conn.cursor()

    cur.execute(
        "SELECT email,name FROM users WHERE id=?",
        (session["user_id"],)
    )
    result=cur.fetchone()
    cur.execute(
        "SELECT pdf_cnt, flashcard_cnt, story_cnt, language_cnt FROM feature_usage WHERE user_id=?",
        (session["user_id"],)
    )
    usage = cur.fetchone()
    conn.close()

    if result:

        email,name=result

        session["email"]=email
        session["name"]=name

    else:
        return "User not found",404
    
    #PRINT KARNEKE LIYE YE LIKHA GAYA HAIIII ------- DEBUGGING TECHNIQUEE
    print(usage)

    if max(usage) == int(usage[0]):
        most_used = "Summary & Quiz"
    elif max(usage) == int(usage[1]):
        most_used = "Flashcard"
    elif max(usage) == int(usage[2]):
        most_used = "Story"
    else:
        most_used = "Language"

    analytics = {
    "summary": usage[0],
    "flashcards": usage[1],
    "stories": usage[2],
    "language": usage[3]
    }

    return render_template(
        "profile.html",
        username=name,
        name=session["name"],
        email=email,
        usage=usage,
        most_used = most_used,
        analytics = analytics
    )