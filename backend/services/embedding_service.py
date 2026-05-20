from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-small",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    return embedding_model