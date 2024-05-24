from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

API_KEY = None

# Create OpenAI embedding instance
embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)

# Load CSV file
loader = CSVLoader(file_path='datasets/restaurants-with-menus-utf8-100k.csv', encoding='utf-8')
raw_documents = loader.load()

# Split raw file into chunks
char_splitter = RecursiveCharacterTextSplitter(
    separators=['\n'],
    chunk_size=200,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False
)
documents = char_splitter.split_documents(raw_documents)

# Create Chroma vector store from the documents and save it on the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(current_dir, "chroma-vector-db")
vector_store = Chroma.from_documents(documents, embeddings, persist_directory=save_dir)
