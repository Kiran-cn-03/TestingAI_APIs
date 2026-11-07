import gradio as gr
from agent import agent 

def chat(message, history):  
    return agent(message)

gr.ChatInterface(fn=chat, title="🛍️ Smart Shop Assistant").launch(share=True) 