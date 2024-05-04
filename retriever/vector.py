from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

api_key = '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'

raw_documents = TextLoader('info.text').load()
text_splitter = CharacterTextSplitter(chunk_size=120, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)

db = FAISS.from_documents(documents, OpenAIEmbeddings(openai_api_key=api_key))

# query = "易居研究院研究总监"
query = "奥迪A4"
docs = db.similarity_search(query)

for doc in docs:
    print(doc)

