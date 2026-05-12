"""
build_index.py ~ pipelines the raw data retrieved from the pull scripts and API sources (Wikipedia, Discogs) and
subsequently stores the data in usable chunks that will not eat up LLMs token limits


RAW DATA -> DOCUMENT FORM -> CHUNKS -> EMBED -> STORE


05/12/26
Author: Nicholas Kennedy
"""






import json
from pathlib import Path


import chromadb




RAW_DIR = Path(__file__).parent.parent / "data" / "raw" / "wikipedia"
CHROMA_DIR = Path(__file__).parent.parent / "chroma_db"

COLLECTION_NAME = "VinylSage"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

CHUNK_SIZE = 512
CHUNK_OVERLAP = 50




def load_documents() -> list[Document]:
    """
    Transform the raw JSON data retrieved in the pull script into list of Documents.
    
    """
    






def build_index():
    pass




