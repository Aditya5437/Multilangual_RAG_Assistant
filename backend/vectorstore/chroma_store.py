from langchain_chroma import Chroma
from backend.services.embedding_service import load_embedding_model

CHROMA_DB_PATH = "data/chroma_db"


def get_vectorstore():

    embedding_model = load_embedding_model()

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model
    )

    return vectorstore