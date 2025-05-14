# ContentSpeciality# 🧠 Specialty Bot

**Specialty Bot** is a minimal, interactive chatbot that delivers unique facts about any topic you ask. Powered by [OpenAI](https://platform.openai.com/) via [LangChain](https://github.com/langchain-ai/langchain), it uses prompt templates to generate high-quality, informative responses from GPT models.

---

## 📌 Key Features

- ✨ OpenAI-powered fact generation
- 🧱 PromptTemplate integration for flexible prompt engineering
- 📦 Lightweight CLI application with no external UI dependencies
- 🔐 Secure environment variable management

---

## 🚀 Getting Started


1. Install Dependencies

  pip install -r requirements.txt Or install manually:

   pip install langchain openai python-dotenv


2. Set Up API Key


📂 Project Structure

specialty-bot/

├── bot.py              # Main Python script

├── .env                # Environment file (ignored by Git)

├── requirements.txt    # Python dependencies

└── README.md           # Project documentation

💡 Usage


 Run the bot using:


   python bot.py


  Then, simply enter a topic:

   Enter a topic: space

  Specialty:
   Space is completely silent because there is no atmosphere to carry sound.
   Type exit or quit to stop the bot.

🧪 Prompt Template Logic

   The chatbot uses the following format to guide the model:


    Tell me a unique or special fact about {topic}.
    This ensures that each response is concise, relevant, and engaging.

❓ Troubleshooting
     No response or empty output
     Check your internet connection and API key validity.

     Module not found errors
     Ensure all dependencies are installed correctly.


     pip install -r requirements









