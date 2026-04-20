from langchain_openai import ChatOpenAI
from src.prompt_template import get_anime_prompt
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma

class AnimeRecommender:
    def __init__(self, vector_store:Chroma, api_key:str, model_name:str):
        self.llm = ChatOpenAI(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()
        _context_chain = (
            {
                "query": RunnablePassthrough()
            }
            | RunnableLambda(lambda x : vector_store.as_retriever(
                    search_type="similarity",   
                    search_kwargs={"k": 5}
                ).invoke(x["query"])
            )
        )
        self.qa_chain = (
            {
                "context": _context_chain,
                "question": RunnablePassthrough()
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
    
    def get_recommendation(self, query:str):
        return self.qa_chain.invoke(query)