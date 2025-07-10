# University FAQ Chatbot

A simple AI-powered chatbot for answering university-related frequently asked questions using Python, ChatterBot, and Flask.

## Features
- Answers common university FAQs
- Web interface for easy interaction
- Easy to extend with more questions

## Setup Instructions

1. **Clone or download this project.**
2. **Create and activate a Python 3.10 virtual environment.**
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Train the chatbot:**
   ```
   python train_chatbot.py
   ```
5. **Run the web app:**
   ```
   python app.py
   ```
6. **Open your browser and go to:**
   http://127.0.0.1:5000/

## Customizing FAQs
- Edit the `custom_faq` list in `train_chatbot.py` to add or change questions and answers.
- Retrain the bot after making changes.

## Notes
- Make sure to use Python 3.10 for best compatibility with ChatterBot.
- All dependencies are listed in `requirements.txt`. 