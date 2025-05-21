# Math-Chat-bot
🤖 Math-Chat-Bot
An AI-powered general-purpose chatbot built with LLMs that can answer any natural language question, including solving math problems. It uses cutting-edge language models to simulate human-like conversations and provide intelligent, context-aware responses.

## 🧠 What It Can Do
-✅ Answer general knowledge questions

-🔢 Solve mathematical problems (arithmetic, algebra, calculus, etc.)

-🧑‍🏫 Explain complex concepts in simple terms

-💬 Hold contextual conversations like a real assistant

-⚙️ Easily extendable to connect with APIs or external tools

## 🚀 Getting Started
### 1). Clone the Repository

git clone https://github.com/Gayatrisjadhav/Math-Chat-bot.git
cd Math-Chat-bot

### 2). Create and Activate Virtual Environment (Recommended)

python -m venv .venv
- Windows
.venv\Scripts\activate
- macOS/Linux
source .venv/bin/activate

### 3). Install Dependencies

If you're using uv, run:

uv pip install -r requirements.txt
Or with pip:

pip install -r requirements.txt
4). Set Up Environment Variables
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here
You may also include keys for other providers like Groq, Gemini, etc., depending on how your bot is configured.

## 💡 Usage
Run the chatbot:


python main.py
Example conversation:


You: What is the capital of France?
Bot: The capital of France is Paris.

You: Solve x^2 + 3x + 2 = 0
Bot: The solutions to the equation are x = -1 and x = -2.
## 📁 Project Structure

Math-Chat-bot/
- ├── main.py              # Chatbot entry point
- ├── pyproject.toml       # uv / poetry / PEP 621 metadata
- ├── requirements.txt     # Project dependencies
- ├── .env                 # Environment variables (not committed)
- └── README.md            # Project documentation
## 🧩 Built With
Python

LangChain

LangGraph

OpenAI API

Groq (optional)

uv for fast dependency management

🤝 Contributing
Contributions are welcome! Feel free to fork the repo, create an issue, or submit a pull request.

📄 License
Licensed under the MIT License.

