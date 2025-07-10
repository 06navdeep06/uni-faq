from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

# Create chatbot instance
chatbot = ChatBot(
    'UniversityFAQBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///university_faq_db.sqlite3'
)

# Train with English corpus data
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

# Custom university FAQ data
custom_faq = [
    [
        "What is the admission process?",
        "The admission process involves submitting an online application, academic transcripts, and required test scores."
    ],
    [
        "What are the tuition fees?",
        "Tuition fees vary by program. Please visit our website or contact the admissions office for details."
    ],
    [
        "Are scholarships available?",
        "Yes, we offer merit-based and need-based scholarships for eligible students."
    ],
    [
        "How can I contact the admissions office?",
        "You can contact the admissions office via email at admissions@university.edu or call +1-234-567-890."
    ]
]

# Train with custom FAQ
list_trainer = ListTrainer(chatbot)
for pair in custom_faq:
    list_trainer.train(pair)

print("Chatbot training complete.") 