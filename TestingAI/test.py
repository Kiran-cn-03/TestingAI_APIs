from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()           # reads OPENAI_API_KEY from .env

client = OpenAI()       # the key is picked up automatically

response = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)
print("── GPT says:", response.choices[0].message.content)
