from flask import Blueprint, render_template, request, session
import sqlite3 as sq
from deep_translator import GoogleTranslator
from essentials import extractpdf

lang = Blueprint("language", __name__)

@lang.route("/language", methods=["GET","POST"])
def language():

    summary=None

    if request.method=="POST":

        target_lang=request.form.get("language")
        text_input=request.form.get("text_input","").strip()

        file=request.files["fileInput"]

        extracted_text=""

        if file and file.filename.endswith(".pdf"):
            extracted_text=extractpdf(file)

        elif text_input:
            extracted_text=text_input

        if extracted_text:

            try:

                translated=GoogleTranslator(
                    source="auto",
                    target=target_lang
                ).translate(extracted_text)

                summary=translated

            except Exception as e:

                summary=f"Error: {str(e)}"
            
            if summary and "user_id" in session:

                conn = sq.connect("users.db")
                cur = conn.cursor()

                cur.execute(
                    "UPDATE feature_usage SET language_cnt = language_cnt + 1 WHERE user_id=?",
                    (session["user_id"],)
                )

                conn.commit()
                conn.close()

    return render_template("language.html",summary=summary)