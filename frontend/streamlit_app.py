import streamlit as st
import requests


FASTAPI_URL = "http://127.0.0.1:8000"




st.set_page_config(
    page_title="Multilingual Government RAG Assistant",
    layout="wide"
)

st.title("Multilingual Government RAG Assistant")

st.markdown(
    """
    Upload government PDFs and ask questions in:
    - English
    - Hindi
    - Marathi
    - Other languages
    """
)

st.divider()




if "messages" not in st.session_state:
    st.session_state.messages = []




with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        with st.spinner("Uploading PDF..."):

            response = requests.post(
                f"{FASTAPI_URL}/upload-pdf",
                files=files
            )

        if response.status_code == 200:

            st.success("PDF Uploaded Successfully!")

            result = response.json()

            st.json(result)

        else:

            st.error("Upload Failed")




st.header(" Ask Questions")


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


user_question = st.chat_input(
    "Ask question in any language..."
)


if user_question and user_question.strip():
    

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    
    with st.chat_message("user"):

        st.markdown(user_question)

    
    payload = {
        "question": user_question
    }

    with st.spinner("Generating answer..."):

        response = requests.post(
            f"{FASTAPI_URL}/ask",
            json=payload
        )

    if response.status_code == 200:

        result = response.json()

        answer = result["answer"]

        retrieved_chunks = result["retrieved_chunks"]

        assistant_response = f"""
{answer}

---
📚 Retrieved Chunks: {retrieved_chunks}
"""

        
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

        
        with st.chat_message("assistant"):

            st.markdown(assistant_response)

    else:

        st.error("Failed to generate response")