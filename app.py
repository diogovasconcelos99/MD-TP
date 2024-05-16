import streamlit as st

# Setup the app title
st.title('Ask UberEatsGPT')

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
    
# @todo