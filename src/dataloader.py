import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
    
    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding="utf-8").dropna()
        required_columns = {"Name", "Genres", "synopsis"}
        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError("Missing columns in data.")
        for index in range(len(df)):
            df.loc[index, "combined_info"] = f"Title: {df.loc[index, 'Name']}, Overview: {df.loc[index, 'synopsis']} Genre: {df.loc[index, 'Genres']}."
        df[["combined_info"]].to_csv(self.processed_csv, index=False, header=False, encoding="utf-8")

        return self.processed_csv

if __name__=="__main__":
    data_loader = AnimeDataLoader("../data/anime_with_synopsis.csv", "../data/anime_processed.csv")
    print(data_loader.load_and_process())