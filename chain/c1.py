from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import utils

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=utils.openai_model, prompt=prompt)

# Run the chain only specifying the input variable.
res1 = chain.invoke("算命")
print(f"llm: {res1}")

# --------- chat_model ---------

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

system_message_prompt = SystemMessagePromptTemplate.from_template(template="You are a AI assistant, you will help ")

# system_message_prompt = SystemMessagePromptTemplate(
#     prompt=PromptTemplate(
#         template="You are a AI assistant, you will help users to get a name for their company."
#     )
# )
#
human_message_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template="What is a good name for a company that makes {product}?",
        input_variables=["product"],
    )
)

chat_prompt_template = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chain = LLMChain(llm=utils.openai_chat_model, prompt=chat_prompt_template)
res2 = chain.invoke("算命")
print(f"res2: {res2}")
