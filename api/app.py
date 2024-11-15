from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama

# Load environment variables
load_dotenv()

# Set necessary environment variables
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Define the Ollama LLM with Llama2
llm = Ollama(model="llama2")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

# Add routes for Llama2-based tasks
add_routes(app, llm, path="/llama2")

add_routes(
    app,
    prompt1 | llm,  # Combine the prompt with the LLM
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,  # Combine the prompt with the LLM
    path="/poem"
)

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
