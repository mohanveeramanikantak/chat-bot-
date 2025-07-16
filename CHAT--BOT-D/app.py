from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Gemini Chat Endpoint
@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "⚠️ Please enter a valid message."}), 400

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(user_input)
        return jsonify({"response": response.text.strip()})
    except Exception as e:
        print("🚨 Error:", e)
        return jsonify({"response": "❌ Something went wrong with the AI."}), 500

# ✅ Home Route (Chat UI)
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Start Flask App
if __name__ == "__main__":
    app.run(debug=True)
