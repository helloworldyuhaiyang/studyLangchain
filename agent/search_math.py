
from langchain import hub
from langchain.agents import load_tools, AgentType, create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

import utils

from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()
# res = search.run("Who is winner of FIFA worldcup 2018?")
# print(res)

prompt = hub.pull("hwchase17/react")
llm = utils.openai_model
tools = load_tools(["ddg-search", "llm-math"], llm=llm)
agent = create_react_agent(tools=tools, llm=llm, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
res2 = agent_executor.invoke({'input': "What is the height difference between Eiffel Tower and Taiwan 101 Tower?"})
print(res2)



