from src.vector_store import AnimeVectorStoreBuilder
from src.recommender import AnimeRecommender
from pipeline.build_pipeline import main
from config.config import MODEL_NAME
import os
from dotenv import load_dotenv

load_dotenv()

class AnimeRecommendationPipeline:
    def __init__(self, persist_directory="chroma_db"):
        try:
            vector_builder = AnimeVectorStoreBuilder(
                csv_filepath="",
                persist_dir=persist_directory
            )
            vector_store = vector_builder.load_vector_store()
            self.recommender = AnimeRecommender(
                vector_store=vector_store,
                api_key=os.getenv("OPENAI_API_KEY"),
                model_name=MODEL_NAME
            )
        except Exception as e:
            raise Exception(e)
    
    def recommend(self, query:str) -> str:
        try:
            recommendation = self.recommender.get_recommendation(query=query)
            return recommendation
        except Exception as e:
            raise Exception(e)
    
    def build_database(self):
        try:
            main()
        except Exception as e:
            raise Exception(e)