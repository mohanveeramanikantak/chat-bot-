 NeoMind AI Chat Assistant

geni is a general-purpose AI-powered chatbot that interacts with users in a friendly and intelligent manner. Built using Python (Flask), google  Gemini API, HTML/CSS/JS for the frontend — it simulates human-like responses for any general queries.

## 🚀 Features

- Chat with an AI assistant powered by Gemini (Google Generative AI)
- Clean, responsive UI with dark theme
- Real-time chat with typing animation
- Chat session memory saved locally (in-browser)
- Sidebar to view, rename, and delete chat histories
- Mobile-friendly layout with toggleable sidebar

---

## ⚙️ Tech Stack

| Frontend              | Backend          | AI Model                     |
|-----------------------|------------------|------------------------------|
| HTML, CSS, JavaScript | Python Flask     | Gemini 2.5 Flash (Google AI) |

---

## 🛠 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/bhavanisankardavuluri10/neomind-ai.git
cd neomind-ai

2. Install Dependencies
pip install -r requirements.txt

3. Configure API Key
Create a .env file in the root folder and add your Gemini API key:  (optinal ) because i gave my apikey in .env current testing if key eceeded the limits then you need to generaate a new key 

GEMINI_API_KEY=your_google_gemini_api_key_here
🔑 Get your key from: https://aistudio.google.com/app/apikey

4. Run the App

python app.py
Visit http://127.0.0.1:5000/chat in your browser to start chatting with NeoMind!

🧪 Usage Guide
Signup/Login to start

Use the sidebar to switch between previous chat sessions

Click + New Chat to start fresh

Toggle the sidebar on small screens using ☰

Logout with the red button at the bottom of sidebar

📁 Folder Structure
arduino
Copy
Edit
geni/
├── static/
│   ├── styles.css
│   ├── script.js
│  
├── templates/
│   ├── index.html
│  
├── app.py
├── requirements.txt
├── .env (not included in repo)
└── README.md


dont forget to install the dependensices in the requiremnets .txt thankyou




