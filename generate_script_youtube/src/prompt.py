from langchain.prompts import PromptTemplate


class Prompt():
    def __init__(self) -> None:
        pass

    def create_prompt(self, template: str, input_variables: list) -> PromptTemplate:

        template = PromptTemplate(
            template=template,
            input_variables=input_variables
        )

        return template
