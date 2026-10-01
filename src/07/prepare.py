from langchain_community.document_loaders import PyPDFLoader
import os
import sys

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

CURRENT_DIR = os.path.dirname(__file__)
INGEST_DIR = os.path.join(CURRENT_DIR, "..", "06")
sys.path.insert(0, INGEST_DIR)

from ingest import load_documents

docs = load_documents("../../data/manual.pdf")

CHUNK_SIZE = 200
CHUNK_OVERLAP = 50

def prepare_chunks(path):
    docs = load_documents(path)
    splitter = RecursiveCharacterTextSplitter(
       chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function = len,
    )

    chunks = splitter.split_documents(docs)

    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] =  index

    print(f"청크 {len(chunks)}개")

    return chunks

if __name__ == "__main__":

    chunks = prepare_chunks("../../data/manual.pdf")

    for chunk in chunks[:3]:
        print(chunk.page_content)
        print(chunk.metadata["chunk_id"])
        print()