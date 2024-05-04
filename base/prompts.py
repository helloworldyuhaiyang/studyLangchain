
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
res = prompt.format(product="colorful socks")
print(res)

