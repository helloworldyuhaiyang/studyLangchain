from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.base import BaseCallbackHandler
import time

import utils


class TimerHandler(BaseCallbackHandler):

    def __init__(self) -> None:
        super().__init__()
        self.previous_ms = None
        self.durations = []

    @staticmethod
    def current_ms():
        return int(time.time() * 1000 + time.perf_counter() % 1 * 1000)

    def on_chain_start(self, serialized, inputs, **kwargs) -> None:
        self.previous_ms = self.current_ms()

    def on_chain_end(self, outputs, **kwargs) -> None:
        if self.previous_ms:
            duration = self.current_ms() - self.previous_ms
            self.durations.append(duration)

    def on_llm_start(self, serialized, prompts, **kwargs) -> None:
        self.previous_ms = self.current_ms()

    def on_llm_end(self, res, **kwargs) -> None:
        if self.previous_ms:
            duration = self.current_ms() - self.previous_ms
            self.durations.append(duration)


llm = utils.openai_model

timerHandler = TimerHandler()
prompt = PromptTemplate.from_template("What is the HEX code of color {color_name}?")
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[timerHandler])
response = chain.invoke(input={'color_name': "blue"})
print(response)
response = chain.invoke(input={'color_name': "purple"})
print(response)

print("Durations:", timerHandler.durations)
