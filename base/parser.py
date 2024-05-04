from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import OpenAI, ChatOpenAI

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, field_validator
from typing import List

api_key = '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'

model = OpenAI(openai_api_key=api_key)


# Define your desired data structure.
class Joke(BaseModel):
    user_input: str = Field(description="the user input.")
    why: str = Field(description="the reason of grammatical mistakes")
    more_native: str = Field(description="more native expression.")

    # You can add custom validation logic easily with Pydantic.
    @field_validator('more_native')
    def question_ends_with_question_mark(cls, field):
        if field[-1] != '?':
            raise ValueError("Badly formed question!")
        return field


# Set up a parser + inject instructions into the prompt template.
output_parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Check the grammar of the user input following the keyword 'g:', "
             "identify the reason for any grammatical mistakes, "
             "and then provide a more native expression."
             "\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

# And a query intended to prompt a language model to populate the data structure.
user_input = "g:did you look it?"
_input = prompt.format_prompt(query=user_input)

output = model.invoke(_input)
res = output_parser.parse(output)

print(res)
