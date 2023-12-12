from langchain.chains import LLMChain, SequentialChain


class CreateChain():
    def __init__(self) -> None:
        pass

    def create(self, prompt, llm, output_key: str = None):
        chain = LLMChain(llm=llm, prompt=prompt, output_key=output_key)
        return chain

    def concatenate_chains(self, chain1, chain2):
        concat_chains = SequentialChain(
            chains=[chain1, chain2],
            input_variables=["topic", "content_wiki"],
            output_variables=["script"]
        )
        return concat_chains
