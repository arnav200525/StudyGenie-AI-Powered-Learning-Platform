## StudyGenie – AI Powered Learning Platform

StudyGenie is an AI-powered learning platform built with Flask that helps students turn traditional study material into interactive learning resources.

The platform allows users to upload academic PDF content and transform it into concise summaries, quizzes, flashcards, translated explanations, and story-based learning formats using Generative AI.

StudyGenie is designed to make studying faster, smarter, and more engaging for students.

---

## Features

### PDF Summarizer
Upload academic PDF files and generate concise AI-powered summaries for quick understanding and revision.

### Quiz Generator
Generate multiple-choice questions (MCQs) from PDF-based study material for self-assessment and exam preparation.

### Flashcard Generator
Convert academic content into AI-generated flashcards for active recall and memory retention.

### Language Translator
Translate educational content into different languages for better accessibility and understanding.

### Story-Based Learning
Transform complex academic topics into simple story-based explanations to improve retention and make learning more engaging.

### User Authentication
Secure registration and login system for personalized access.

### User Profile Dashboard
Track learning activity and feature usage through a personalized profile section.

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

### Backend
- Python
- Flask

### Database
- SQLite

### AI / Libraries
- Google Generative AI
- PDFPlumber
- Deep Translator
- gTTS (Google Text-to-Speech)

---

## Project Structure

```bash
StudyGenie-AI-Powered-Learning-Platform/
│
├── app.py                  # Main Flask application
├── database.py             # Database setup and initialization
├── essentials.py           # Shared helper functions
├── requirements.txt        # Project dependencies
├── users.db                # SQLite database
│
├── routes/                 # Flask blueprints
│   ├── authentication.py   # Login and registration routes
│   ├── pdf_summary.py      # PDF summarization and quiz generation
│   ├── flashcards.py       # Flashcard generation
│   ├── lang.py             # Translation functionality
│   ├── story.py            # Story-based learning
│   ├── profile.py          # User dashboard/profile
│   └── static.py           # Static page routes
│
├── templates/              # Frontend templates
│   ├── index.html
│   ├── welcome.html
│   ├── login.html
│   ├── register.html
│   ├── pdfsummarise.html
│   ├── flashcard.html
│   ├── language.html
│   ├── storyy.html
│   ├── profile.html
│   └── features.html
│
└── Documentation/          # Project documentation
    ├── Final_Documentation.pdf
    ├── Final_Documentation.docx
    ├── dfd.docx
    ├── erd.docx
    ├── state.docx
    ├── use case.docx
    └── activity.docx
```
---

## How It Works

1. User registers and logs into the platform.  
2. User selects a learning feature.  
3. User uploads academic PDF content.  
4. The system extracts text from the PDF.  
5. AI processes the content based on the selected feature:  
   - Summarization  
   - Quiz Generation  
   - Flashcards  
   - Translation  
   - Story Conversion  
6. Processed output is displayed in an interactive format.  
7. User activity is tracked in the profile dashboard.  

---

## Future Improvements

- Password hashing for better security  
- Download generated outputs (PDF / TXT)  
- Save learning history  
- Dark mode UI  
- Improved analytics dashboard  
- Support for DOCX and TXT files  
- AI chatbot for doubt solving  
- Voice-based interaction  

---

## Documentation

Detailed project documentation is included in the `Documentation/` folder, including:

- Final Project Report  
- DFD  
- ERD  
- Use Case Diagram  
- State Diagram  
- Activity Diagram  

---

## Disclaimer

This project is built for academic and educational purposes.  
AI-generated responses may require manual verification depending on the complexity of the source material.  

---

## Author

Developed as an academic project focused on improving student learning through AI-powered educational tools.

<img width="1920" height="1080" alt="Screenshot (277)" src="https://github.com/user-attachments/assets/0a12a0fd-18c9-4c68-971a-4ee8c227511c" />
<img width="1920" height="1080" alt="Screenshot (278)" src="https://github.com/user-attachments/assets/d14648f8-3d55-40be-aa97-5ca2d8d39fa9" />
<img width="1920" height="1080" alt="Screenshot (280)" src="https://github.com/user-attachments/assets/1d149dc7-6c44-4947-9a5e-5c9a5391096e" />
<img width="1920" height="1080" alt="Screenshot (282)" src="https://github.com/user-attachments/assets/ac7fa357-919e-49de-80fb-35c9a6c3b01e" />
<img width="1920" height="1080" alt="Screenshot (283)" src="https://github.com/user-attachments/assets/bc8eb609-a269-4e9e-bd6b-372aa144f02d" />




