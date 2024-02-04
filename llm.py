import os
from typing import Any
from dotenv import load_dotenv, find_dotenv


from langchain.chat_models.azure_openai import AzureChatOpenAI
from langchain.chat_models.ollama import ChatOllama
from langchain.llms.huggingface_hub import HuggingFaceHub


path_to_env_file = find_dotenv()
load_dotenv(path_to_env_file)

# TODO ===> replace "get_model" with "__call__"
class LLMProvider:
    def __init__(self, provider = "openai") -> None:
        # init env vars required for running LLM
        self.provider = provider
        self.temperature = 0.0

    def get_model(self):
        if self.provider == "openai":
            return AzureChatOpenAI(
                openai_api_key=os.environ.get("OPENAI_API_KEY"),
                openai_api_base=os.environ.get("OPENAI_API_BASE"),
                deployment_name=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
                temperature=self.temperature,
            )

        if self.provider == "hugging_face":
            return HuggingFaceHub(
                repo_id="HuggingFaceH4/zephyr-7b-beta",
                task="text-generation",
                model_kwargs={
                    "temperature": 0.1,
                    "repetition_penalty": 1.03,
                },
            )

        if self.provider == "ollama":
            # NOTE: This needs local installation of ollama models
            return ChatOllama(model="llama2:7b-chat", temperature=self.temperature)
        



if __name__ == "__main__":
    from langchain.schema import HumanMessage
    message = HumanMessage(content="Translate this sentence from English to French. I love programming.")
    
