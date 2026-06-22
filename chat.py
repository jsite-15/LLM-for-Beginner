from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506", temperature=0.9,max_tokens=20)

response = model.invoke("write a poem on ai")

print(response.content)


