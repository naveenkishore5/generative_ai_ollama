from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from langchain_community.llms import FakeListLLM

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='A simple Fast API server'
)

# add_routes(
#     app,
#     FakeListLLM(),
#     path='/fake_llm'
# )

responses = [
    "Hello, how can I help you?",
    "Sure, let me assist you with that.",
    "I'm sorry, I don't have the information you're looking for."
]

model1 = FakeListLLM(responses=responses)
llm = Ollama(model='llama2')

# chat prompt for model1

prompt1 = ChatPromptTemplate.from_template("Write me a song {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a song {topic} with 100 words")

add_routes(
    app,
    prompt1 | model1,
    path='/song'
)

add_routes(
    app,
    prompt2 | llm,
    path='/topten'
)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8085)