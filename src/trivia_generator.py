# src/trivia_generator.py
from openai import ChatCompletion
from config.settings import OPENAI_API_KEY, CUSTOM_MODEL

def generate_trivia(keyword):
    prompt = f"{keyword}についての興味深い事実を教えてください。"
    response = ChatCompletion.create(engine=CUSTOM_MODEL, prompt=prompt, max_tokens=150)
    text = response.choices[0].text.strip()
    title, content = text.split('\n', 1)
    return title.strip(), content.strip()