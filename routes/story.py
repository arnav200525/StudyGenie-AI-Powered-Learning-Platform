from flask import Blueprint, render_template, request, session
import sqlite3 as sq
from essentials import extractpdf, model
from gtts import gTTS

story = Blueprint("story", __name__)

@story.route("/storyy", methods=["GET","POST"])
def upload_pdf2():

    storyyy=None
    audio_file=None

    if request.method=="POST":

        pdf_file=request.files["pdf_file"]

        if pdf_file.filename!="":

            extracted_text=extractpdf(pdf_file)

            prompt_story=f"""
Turn the following text into a memorable story.

Text:
{extracted_text}
"""

            response=model.generate_content(prompt_story)

            storyyy=response.text.replace("#","")

            if storyyy:

                tts=gTTS(storyyy)
                audio_file="static/AIStory.mp3"
                tts.save(audio_file)
                
            if storyyy and "user_id" in session:

                conn = sq.connect("users.db")
                cur = conn.cursor()

                cur.execute(
                    "UPDATE feature_usage SET story_cnt = story_cnt + 1 WHERE user_id=?",
                    (session["user_id"],)
                )

                conn.commit()
                conn.close()

    return render_template("storyy.html",strr=storyyy,audio_file=audio_file)