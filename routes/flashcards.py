from flask import Blueprint, render_template, request, session
import sqlite3 as sq
from essentials import extractpdf, model

flashcard = Blueprint("flash", __name__)

@flashcard.route("/flashcards", methods=["GET","POST"])
def flash():

    f_output=[]

    if request.method=="POST":

        pdf=request.files["pdffile"]
        n_cards=request.form["n_cards"]

        pdf_text=extractpdf(pdf)

        if n_cards=="":
            n_cards=12

        prompt=f"""
Generate {n_cards} flashcards.

Format:
Q: question
A: answer

Text: {pdf_text}
"""

        response=model.generate_content(prompt)

        lines=response.text.split("\n")

        question=""
        answer=""

        for line in lines:

            if line.startswith("Q:"):
                question=line.replace("Q:","")

            elif line.startswith("A:"):
                answer=line.replace("A:","")

                if question and answer:

                    f_output.append({
                        "q":question,
                        "a":answer
                    })

                    question=""
                    answer=""
                    
        if f_output and "user_id" in session:

            conn = sq.connect("users.db")
            cur = conn.cursor()

            cur.execute(
                "UPDATE feature_usage SET flashcard_cnt = flashcard_cnt + 1 WHERE user_id=?",
                (session["user_id"],)
            )

            conn.commit()
            conn.close()

    return render_template("flashcard.html",flashcard=f_output)