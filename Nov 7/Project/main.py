from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()

app = FastAPI(title="AI Topic Assistant")

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenRouter settings
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DEFAULT_MODEL = "meta-llama/llama-3-8b-instruct"


# Input model
class Query(BaseModel):
    topic: str
    question: str
    model: str | None = None


@app.post("/ask")
async def ask_question(query: Query):
    """
    Accepts topic, question, and optional model — sends to OpenRouter and returns the model’s reply.
    """
    try:
        combined_prompt = (
            f"Topic: {query.topic}\n\n"
            f"Question: {query.question}\n\n"
            "Please respond helpfully and concisely."
        )

        model = query.model or DEFAULT_MODEL
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a kind and helpful assistant."},
                {"role": "user", "content": combined_prompt},
            ],
            "temperature": 0.7,
            "max_tokens": 500,
        }

        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        answer = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )

        if not answer:
            return {"error": "Model returned an empty response. Try a clearer or longer question."}

        return {
            "topic": query.topic,
            "question": query.question,
            "model": model,
            "response": answer,
        }

    except Exception as e:
        return {"error": str(e)}


# Frontend with Model Selector
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>AI Topic Assistant</title>
      <style>
        body {
          font-family: 'Poppins', sans-serif;
          background: linear-gradient(135deg, #ffe6f0, #e6f7ff);
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
          color: #333;
        }
        h1 {
          color: #ff7aa8;
          margin-bottom: 10px;
          text-shadow: 1px 1px 2px rgba(255, 182, 193, 0.4);
        }
        #chat-box {
          width: 90%;
          max-width: 650px;
          height: 60vh;
          background: #fffafc;
          border-radius: 20px;
          padding: 20px;
          overflow-y: auto;
          box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
          display: flex;
          flex-direction: column;
        }
        .msg {
          margin: 10px 0;
          padding: 12px 16px;
          border-radius: 16px;
          line-height: 1.5;
          max-width: 75%;
          animation: fadeIn 0.3s ease;
        }
        .user {
          background: #cdeaff;
          align-self: flex-end;
          border-top-right-radius: 0;
        }
        .bot {
          background: #ffe0eb;
          align-self: flex-start;
          border-top-left-radius: 0;
        }
        #input-area {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 10px;
          width: 90%;
          max-width: 650px;
          margin-top: 15px;
        }
        .input-row {
          display: flex;
          width: 100%;
          gap: 8px;
        }
        input, select {
          flex: 1;
          padding: 12px;
          border-radius: 14px;
          border: 1px solid #ccc;
          font-size: 16px;
        }
        button {
          padding: 12px 20px;
          background: #ff92b0;
          color: white;
          border: none;
          border-radius: 14px;
          cursor: pointer;
          transition: 0.3s;
        }
        button:hover {
          background: #ff7aa8;
        }
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .loading {
          display: inline-block;
          width: 1em;
          height: 1em;
          border: 3px solid #ffb6c1;
          border-radius: 50%;
          border-top-color: transparent;
          animation: spin 1s linear infinite;
          margin-left: 10px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        label {
          font-size: 14px;
          color: #666;
          margin-bottom: 4px;
        }
      </style>
    </head>
    <body>
      <h1>AI Topic Assistant</h1>
      <div id="chat-box"></div>

      <div id="input-area">
        <div class="input-row">
          <input id="topic" placeholder="Enter topic..." />
          <input id="question" placeholder="Ask a question..." />
        </div>
        <div class="input-row">
          <select id="model">
            <option value="mistralai/mistral-7b-instruct">🪶 Mistral 7B Instruct (Fast)</option>
            <option value="meta-llama/llama-3-8b-instruct" selected>🦙 LLaMA 3 8B Instruct (Balanced)</option>
            <option value="google/gemini-flash-1.5">🌟 Gemini 2 Flash (Conversational)</option>
          </select>
          <button onclick="ask()">💌 Ask</button>
        </div>
      </div>

      <script>
        async function ask() {
          const topic = document.getElementById("topic").value.trim();
          const question = document.getElementById("question").value.trim();
          const model = document.getElementById("model").value;
          const chatBox = document.getElementById("chat-box");

          if (!topic || !question) return alert("Please enter both topic and question 💭");

          const userMsg = document.createElement("div");
          userMsg.classList.add("msg", "user");
          userMsg.textContent = `(${topic}) ${question}`;
          chatBox.appendChild(userMsg);

          const botMsg = document.createElement("div");
          botMsg.classList.add("msg", "bot");
          botMsg.innerHTML = 'Thinking<span class="loading"></span>';
          chatBox.appendChild(botMsg);
          chatBox.scrollTop = chatBox.scrollHeight;

          try {
            const res = await fetch("/ask", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ topic, question, model }),
            });
            const data = await res.json();
            botMsg.textContent = data.response || data.error || "No reply.";
          } catch (err) {
            botMsg.textContent = "❌ Error: " + err.message;
          }

          chatBox.scrollTop = chatBox.scrollHeight;
        }
      </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


