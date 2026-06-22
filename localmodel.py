from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs = dict(
         max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )

)


chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("what is data science ?")

print(result.content)