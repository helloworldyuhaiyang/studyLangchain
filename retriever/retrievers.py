from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings

api_key = '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'

embedding = OpenAIEmbeddings(openai_api_key=api_key)
model = OpenAI(openai_api_key=api_key)

from langchain_community.document_loaders import TextLoader

loader = TextLoader('../state_of_the_union.txt', encoding='utf8')

from langchain.indexes import VectorstoreIndexCreator

## 一行代码 创建索引
index = VectorstoreIndexCreator(
    embedding=embedding,
).from_loaders([loader])

query = "What did the president say about Ketanji Brown Jackson"
res = index.query_with_sources(question=query, llm=model)

print(res)
