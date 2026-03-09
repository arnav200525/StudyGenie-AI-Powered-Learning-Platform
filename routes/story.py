from flask import Blueprint, render_template, request
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

    return render_template("storyy.html",strr=storyyy,audio_file=audio_file)