from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from config.config import EMBEDDING_MODEL
import os, shutil

load_dotenv()

class AnimeVectorStoreBuilder:
    def __init__(self, csv_filepath:str, persist_dir:str="chroma_db"):
        self.csv_path = csv_filepath
        self.persist_dir = persist_dir
        self.embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    
    def create_vector_store(self):

        if os.path.exists(self.persist_dir):
            shutil.rmtree(self.persist_dir)

        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
        )

        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

        chunks = splitter.split_documents(data)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_dir
        )
    
    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)