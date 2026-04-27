from flask import Flask
from database import database

from routes.authentication import auth
from routes.static import static
from routes.pdf_summary import pdf
from routes.flashcards import flashcard
from routes.lang import lang
from routes.story import story
from routes.profile import profile

app = Flask(__name__)
app.secret_key = "Academic_Project"

database()

app.register_blueprint(static)
app.register_blueprint(auth)
app.register_blueprint(pdf)
app.register_blueprint(flashcard)
app.register_blueprint(lang)
app.register_blueprint(story)
app.register_blueprint(profile)

if __name__ == "__main__":
    app.run(debug=True)