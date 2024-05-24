import os
import streamlit as st
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI, OpenAIEmbeddings


# Get OpenAI API key
API_KEY = None

# Create LLM using Langchain
llm = OpenAI(
    api_key=API_KEY,
    max_tokens=500,
    temperature=0
)

# Vector store loading function
@st.cache_resource
def load_vector_db():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chroma_dir = os.path.join(current_dir, "chroma-vector-db")
    embeddings = OpenAIEmbeddings(api_key=API_KEY)
    vector_store = Chroma(embedding_function=embeddings, persist_directory=chroma_dir)
    return vector_store

# Load vector store
vector_store = load_vector_db()

# Create Q&A chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(),
    input_key='question'
)

# Setup the app title
st.title('Ask UberEatsGPT')

# test_query = "Sample query to test vector store"
# results = vector_store.similarity_search(test_query)
# st.write("Retrieved documents:", results)

# Setup state session to display all messages
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
# Display all the messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Build prompt input template to display prompts
prompt = st.chat_input('Write your prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    response = chain.run(prompt)
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append({'role': 'assistant', 'content': response})
