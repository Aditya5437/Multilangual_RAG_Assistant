import os
from pathlib import Path



list_of_directories = [
    "frontend",
    "backend",
    "backend/services",
    "backend/rag",
    "backend/vectorstore",
    "backend/uploaded_pdfs",
    "backend/routes",
    "backend/utils",
    "data",
    "data/raw_pdfs",
    "data/chroma_db",
]

list_of_files = [
    "frontend/streamlit_app.py",

    "backend/app.py",
    "backend/requirements.txt",

    "backend/services/__init__.py",
    "backend/rag/__init__.py",
    "backend/vectorstore/__init__.py",
    "backend/routes/__init__.py",
    "backend/utils/__init__.py",

    "requirements.txt",

    ".env",
    ".gitignore",
    "README.md",
]



for directory in list_of_directories:
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    print(f"Directory Created: {dir_path}")



for file in list_of_files:
    file_path = Path(file)

   
    file_path.parent.mkdir(parents=True, exist_ok=True)

   
    if not file_path.exists():
        file_path.touch()
        print(f"File Created: {file_path}")

    else:
        print(f"Already Exists: {file_path}")