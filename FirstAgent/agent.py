import json
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

PRICES = {"shoes": 799, "hat": 399, "bag": 1420, "shorts": 1299, "pants": 1699}

def get_price(item):
    print(f"🔧 tool called: get_price({item})")     # so you SEE it happen
    return f"₹{PRICES.get(item.lower(), 'unknown')}"

tools = [{
    "type": "function",                                      # ①
    "function": {
        "name": "get_price",                                 # ②
        "description": "Get the price of a shop item the user asks about.",  # ③
        "parameters": {                                       # ④
            "type": "object",
            "properties": {"item": {"type": "string", "description": "the item name"}},
            "required": ["item"],
        },
    },
}]

def agent(user_message):
    messages = [{"role": "user", "content": user_message}]

    response = groq_client.chat.completions.create(          # ① send message + tools menu
        model="openai/gpt-oss-120b", messages=messages, tools=tools)
    msg = response.choices[0].message

    if msg.tool_calls:                                  # ② did it ask for a tool?
        messages.append(msg)
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)  # ③ read its request, run it
            result = get_price(args["item"])
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
        response = groq_client.chat.completions.create(      # ④ send it all back → nice answer
            model="openai/gpt-oss-120b", messages=messages)
        msg = response.choices[0].message

    return msg.content

print(agent("How much are the shoes?"))     
print(agent("Hi! What can you help with?"))   