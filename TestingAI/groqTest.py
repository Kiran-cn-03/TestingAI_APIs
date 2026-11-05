import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   
groq_client = OpenAI(
    api_key=os.getenv("GROQ_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)
print("── Llama says:", response.choices[0].message.content)