from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you ? ")

print(response.content)

