from langchain_community.document_loaders import BiliBiliLoader
loader = BiliBiliLoader(["https://www.bilibili.com/video/BV1xt411o7Xu/"])

res = loader.load()

print(res)