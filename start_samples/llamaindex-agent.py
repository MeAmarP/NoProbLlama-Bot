from datetime import datetime

from llama_index.llms import Ollama
from llama_index.llms import Cohere

from llama_index.agent import ReActAgent
from llama_index.tools import FunctionTool


def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


# def agent(message, history):
#     agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True)
#     response = agent.chat(message)
#     return response

multiply_tool = FunctionTool.from_defaults(fn=multiply, name="multiply", description="Use this tool to multiply two integers")

add_tool = FunctionTool.from_defaults(fn=add, name="add", description="Use this tool to add two integers")


tools = [multiply_tool, add_tool]

# llm = Ollama(model="llama2", temperature=0.0)

# TODO --> get api key from .env
llm2 = Cohere(api_key=api_key, temperature=0.0)

agent = ReActAgent.from_tools(tools=tools, llm=llm2, verbose=True)
response = agent.chat("Use the provided tools to solve the problem. Problem: What is 10*2? Calculate step by step")
print(response)
