from flask import Flask, request, jsonify, render_template_string
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

# Load the trained chatbot
chatbot = ChatBot(
    'UniversityFAQBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///university_faq_db.sqlite3'
)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>University FAQ Chatbot</title>
</head>
<body>
    <h2>University FAQ Chatbot</h2>
    <form id="chat-form">
        <input type="text" id="user-input" placeholder="Ask a question..." autocomplete="off" required>
        <button type="submit">Send</button>
    </form>
    <div id="chat-box"></div>
    <script>
        const form = document.getElementById('chat-form');
        const input = document.getElementById('user-input');
        const chatBox = document.getElementById('chat-box');
        form.onsubmit = async (e) => {
            e.preventDefault();
            const userText = input.value;
            chatBox.innerHTML += `<b>You:</b> ${userText}<br>`;
            input.value = '';
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userText })
            });
            const data = await res.json();
            chatBox.innerHTML += `<b>Bot:</b> ${data.reply}<br>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        };
    </script>
</body>
</html>
'''

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = str(chatbot.get_response(user_message))
    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(debug=True) 