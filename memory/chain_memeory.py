from langchain.chains.llm import LLMChain
from utils import llm_model
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

template = """You are a chatbot having a conversation with a human.

{chat_history}

Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=llm_model,
    prompt=prompt,
    verbose=True,
    memory=memory,
)

llm_chain.predict(human_input="Hi there my friend")

print(memory.chat_memory)

llm_chain.predict(human_input="Not too bad - how are you?")

print(memory.chat_memory)

