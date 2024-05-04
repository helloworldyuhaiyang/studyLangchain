from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

import utils

with open("../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)


docsearch = Chroma.from_texts(
    texts, utils.openai_embedding, metadatas=[{"source": i} for i in range(len(texts))]
)
query = "What did the president say about Justice Breyer"
docs = docsearch.similarity_search(query)

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

template = """You are a chatbot having a conversation with a human.

Given the following extracted parts of a long document and a question, create a final answer.

{context}

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input", "context"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")

# 会将 docs 传到 prompt 的 {context} 中
chain = load_qa_chain(
    utils.llm_model, chain_type="stuff", memory=memory, prompt=prompt
)

# 用户输入和 文档输入
query = "What did the president say about Justice Breyer"
chain({"input_documents": docs, "human_input": query})

print(chain.memory.buffer)

