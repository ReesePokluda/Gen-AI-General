import gradio as gr
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")
openai_model = 'gpt-4o-mini' 
client = OpenAI(api_key = api_key)

def chatgpt_response(question):
    chat_completion = client.chat.completions.create(
        model=openai_model,
        messages=[{"role": "user", "content": question}]
    )
    return chat_completion.choices[0].message.content

interface = gr.Interface(
    inputs = gr.Textbox(label="Ask a question"),
    fn = chatgpt_response,
    outputs = gr.Textbox(label="Response"),
    title = "My Bot",
    description = "The start of our chatbot"
)

interface.launch()