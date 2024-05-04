# 而在 Agent 中，语言模型被用作推理引擎，来确定应该执行哪些动作以及以何种顺序执行。

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

import utils

llm = utils.openai_model

# 接下来，让我们加载一些要使用的工具。请注意，llm-math 工具使用了一个 LLM，所以我们需要传递它。
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 创建代理，传入工具、模型、代理类型，开启调试
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

res = agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

print(res)
