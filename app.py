import streamlit as st
from chatbot import MentalHealthBot

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = MentalHealthBot()

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("Mental Health Support Chatbot")

# Display chat disclaimer
st.markdown("""
    *Disclaimer*: This chatbot is for informational purposes only and is not a substitute 
    for professional medical advice, diagnosis, or treatment. If you're experiencing a mental 
    health emergency, please contact emergency services or crisis helpline immediately.
""")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How are you feeling today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        response = st.session_state.chatbot.get_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Add crisis resources
st.sidebar.title("Crisis Resources")
st.sidebar.markdown("""
    - *Emergency*: 911
    - *National Suicide Prevention Lifeline*: 988
    - *Crisis Text Line*: Text HOME to 741741
""")
