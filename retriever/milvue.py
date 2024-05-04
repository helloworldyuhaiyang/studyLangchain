from langchain_community.vectorstores import Milvus
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

# init model and embedding
api_key = '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'
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
model = OpenAI(openai_api_key=api_key)


# get documents
loader = TextLoader("../state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vector_db = Milvus.from_documents(
    docs,
    embeddings,
    connection_args={"host": "127.0.0.1", "port": "19530"},
)

query = "总统对Ketanji Brown Jackson说了什么"
docs = vector_db.similarity_search(query)

print(docs)
