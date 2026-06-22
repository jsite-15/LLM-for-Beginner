from dotenv import load_dotenv
from pathlib import Path
import os
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

print("chosse your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")

choice = int(input("tell your response :- "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."


model = ChatMistralAI(model = "mistral-small-2506", temperature=0.9)
messages = [
    SystemMessage(content=mode)
]
from langchain_core.messages import HumanMessage, AIMessage

print("Welcome (Type 0 to exit the application)")
while True:
    prompt = input("You : ")
    if prompt == "0":
        break
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    print("Bot : ",response.content)
    messages.append(AIMessage(content=response.content))
