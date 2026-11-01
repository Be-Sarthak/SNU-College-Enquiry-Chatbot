import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="SNU College Enquiry Chatbot",
    page_icon="🎓"
)

st.title("🎓 SNU College Enquiry Chatbot")
st.write("Welcome! Ask me anything about Sister Nivedita University.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to SNU. How can I help you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Ask your question here...")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    answer = get_response(user_question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()