
from llama_index.llms import Ollama
from llama_index.llms import ChatMessage

from llama_index.tools import FunctionTool
from llama_index.agent import ReActAgent

from datetime import datetime

import gradio as gr

class noprobllema():
    def __init__(self):
        self.llm = Ollama(model="llama2")
        function_tool = FunctionTool.from_defaults(fn=self.get_today_date)
        self.tools = [function_tool]
        
        

    def chat(self, message, history):
        msg = [
            ChatMessage(role="system", content="You are Intelligent AI Chatbot! You are Honest, Helpful and Harmless!"),
            ChatMessage(role="user", content=message)]

        # TODO : Use streamimg to get the response
        resp_bot = self.llm.chat(msg)
        return resp_bot.dict()['message']['content']
    


    


    

run_bot = noprobllema()
demo = gr.ChatInterface(run_bot.chat, title="NoProbLlama! Intelligent AI Chatbot")


def main():
    demo.queue().launch()


if __name__ == "__main__":
    main()
