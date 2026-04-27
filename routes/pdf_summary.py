from flask import Blueprint, render_template, request, session
import sqlite3 as sq
from essentials import extractpdf, model
import json
import re

pdf = Blueprint("pdf", __name__)

@pdf.route("/pdfsumm", methods=["GET","POST"])
def upload_pdf():

    summary=None
    quiz=None

    if request.method=="POST":

        pdf_file=request.files["pdf_file"]

        if pdf_file.filename!="":

            extracted_text=extractpdf(pdf_file)

            prompt_sum=f"Summarize the following text display:\n\n{extracted_text}"

            response=model.generate_content(prompt_sum)

            summary=response.text.replace("*","").replace("#","")

            prompt_mcq=f"""
Generate exactly 10 MCQs from this summary.

Return ONLY JSON format.

Text: {summary}
"""

            response_mcq=model.generate_content(prompt_mcq)

            try:

                clean_text=re.sub(r"```(json)?","",response_mcq.text).strip()

                match=re.search(r"\[.*\]",clean_text,re.S)

                if match:
                    clean_text=match.group(0)

                quiz=json.loads(clean_text)

            except:
                quiz=[]

            if summary and "user_id" in session:

                conn = sq.connect("users.db")
                cur = conn.cursor()

                cur.execute(
                    "UPDATE feature_usage SET pdf_cnt = pdf_cnt + 1 WHERE user_id=?",
                    (session["user_id"],)
                )

                conn.commit()
                conn.close()

    return render_template("pdfsummarise.html",summ=summary,quiz=quiz)