import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
llm = OpenAI(openai_api_key=api_key, temperature=0.7)

# Define prompt template
template = PromptTemplate(
    input_variables=["topic"],
    template="Tell me a unique or special fact about {topic}."
)

# Loop to interact
print("Specialty Bot is ready! Type a topic or 'exit' to quit.\n")
while True:
    topic = input("Enter a topic: ")
    if topic.lower() in ["exit", "quit"]:
        break
    prompt = template.format(topic=topic)
    response = llm(prompt)
    print("\nSpecialty:", response.strip(), "\n")