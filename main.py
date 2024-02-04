from llm import LLMProvider
from tools import DateTimeTool, GoogleSearchTool

from langchain.agents import initialize_agent, AgentType
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

# * Init LLM model
llm = LLMProvider("openai").get_model()
# print(llm.invoke("Hello, Who are you?").content)

# * Init Tools for LLM
tools = [DateTimeTool(), GoogleSearchTool()]


# * Init Memory for LLM
# initialize conversational memory
conversational_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
)


# * Init Agent
agent = initialize_agent(
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    max_iterations=5,
    verbose=True,
    early_stopping_method='generate',
    memory=conversational_memory,
)

respone = agent.invoke("<INST>Use provided list of tools to get answer </INST> Important Websites of Maharashtra")

print(respone["output"])
