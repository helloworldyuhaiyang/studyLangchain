
from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import utils

handler = StdOutCallbackHandler()
llm = utils.openai_model

prompt = PromptTemplate.from_template("Who is {name}?")
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
res = chain.run(name="Super Mario")
print(res)
