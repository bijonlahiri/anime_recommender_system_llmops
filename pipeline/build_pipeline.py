from src.dataloader import AnimeDataLoader
from src.vector_store import AnimeVectorStoreBuilder
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        loader = AnimeDataLoader(
            original_csv="data/anime_with_synopsis.csv",
            processed_csv="data/anime_processed.csv"
        )

        processed_file = loader.load_and_process()

        vector_builder = AnimeVectorStoreBuilder(csv_filepath=processed_file)
        vector_builder.create_vector_store()

    except Exception as e:
        raise Exception(e)

if __name__=="__main__":
    main()