"""
LCEL 使构建复杂链条变得简单。它通过提供以下内容实现这一点：

统一接口：每个 LCEL 对象都实现了Runnable接口，它定义了一组常见的调用方法（invoke、batch、stream、ainvoke等）。这使得 LCEL 对象链也能自动支持这些调用。也就是说，每个 LCEL 对象链本身就是一个 LCEL 对象。
组合原语：LCEL 提供了许多原语，使得组合链条、并行化组件、添加备选方案、动态配置链条内部等变得容易。
"""

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import utils

prompt = ChatPromptTemplate.from_template("告诉我关于{topic}的一个短笑话")
model = utils.openai_model
output_parser = StrOutputParser()

chain = (
    {"topic": RunnablePassthrough()} | prompt | model | output_parser
)

res = chain.invoke("冰淇淋")

print(res)
