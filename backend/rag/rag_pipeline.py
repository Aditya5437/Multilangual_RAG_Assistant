from backend.services.pdf_loader import load_and_split_pdf
from backend.vectorstore.chroma_store import get_vectorstore
from backend.services.llm_service import load_llm


# =========================
# PDF INGESTION
# =========================

def ingest_pdf(pdf_path):

    chunks = load_and_split_pdf(pdf_path)

    vectorstore = get_vectorstore()

    vectorstore.add_documents(chunks)

    return len(chunks)


# =========================
# ASK QUESTION
# =========================

def ask_question(query):

    # Load Vector DB
    vectorstore = get_vectorstore()

    # Similarity Search
    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    # Combine Context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Prompt
    prompt = f"""
    You are a multilingual government scheme assistant.

    Use the provided context to answer the question.

    If the user asks in Hindi, answer in Hindi.
    If the user asks in Marathi, answer in Marathi.
    If the user asks in English, answer in English.
    If the user asks in Tamil, answer in Tamil.

    Context:
    {context}

    Question:
    {query}
    """

    # Load LLM
    llm = load_llm()

    # Generate Response
    response = llm.invoke(prompt)

    return {
        "question": query,
        "answer": response.content,
        "retrieved_chunks": len(docs)
    }