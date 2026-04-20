from src.dataloader import AnimeDataLoader
from src.vector_store import AnimeVectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import MODEL_NAME
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from anime-recommender!")

    data_loader = AnimeDataLoader(original_csv="data/anime_with_synopsis.csv", processed_csv="data/anime_processed.csv")
    processed_file = data_loader.load_and_process()
    vector_store = AnimeVectorStoreBuilder(csv_filepath=processed_file)
    vector_store.create_vector_store()
    vector_store_db = vector_store.load_vector_store()
    recommender = AnimeRecommender(
        vector_store=vector_store_db,
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name=MODEL_NAME
    )
    while True:
        user_query = input("> ")
        print(recommender.get_recommendation(user_query))


if __name__ == "__main__":
    main()
