from langchain_openai import OpenAI, ChatOpenAI
from langchain_openai import OpenAIEmbeddings

api_key = 'sk-b8RFPE6igqg3KIJj696eD4Ca168d4e3d82CfC74797B63a05'

llm_model = OpenAI(
    base_url="https://api.xty.app/v1",
    openai_api_key=api_key,
)

chat_model = ChatOpenAI(
    base_url="https://api.xty.app/v1",
    openai_api_key=api_key,
)

openai_embedding = OpenAIEmbeddings(
    base_url="https://api.xty.app/v1",
    openai_api_key=api_key,
)
