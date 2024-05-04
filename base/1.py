from langchain_openai import OpenAI, ChatOpenAI

api_key = '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'

ai = OpenAI(openai_api_key=api_key)
chat_model = ChatOpenAI(openai_api_key=api_key)


res = ai.invoke("hi, who are you")
print(res)

res2 = chat_model.invoke("hi, who are you")
print(res2)
