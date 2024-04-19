import json
import streamlit as st
import requests
from custom_logger import get_logger

logger = get_logger('frontend')


def create_database_page():
    """Page for creating a database."""
    st.title("Create Database")
    url = st.text_input("Enter Wiki URL")
    if st.button("Submit"):
        response = requests.post("http://localhost:8001/createdb", json={"url": url})
        if response.status_code == 200:
            st.success("Database created successfully")
        else:
            st.error("Error creating database")


def ask_question_page():
    """Page for asking a question."""
    st.title("Ask Wiki Question")
    query = st.selectbox("Suggested questions", ["What is artificial intelligence?",
                                                 "Where is AI technology used?",
                                                 "Which applications make use of advance AI?",
                                                 "Who was the first person to conduct substantial research on AI?",
                                                 "What are knowledge representation and knowledge engineering?",
                                                 "What is a knowledge base?",
                                                 "What is a rational 'Agent'?"])
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("How can I help you today?")
    if prompt:
        with st.chat_message("user", avatar="🙎🏼"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = requests.post("http://localhost:8001/ask", data=json.dumps({"query": prompt.lower()}))
        with st.chat_message("assistant", avatar="🧐"):
            st.markdown(response.json())

        st.session_state.messages.append({"role": "assistant", "content": response.json()})


def main():
    """Main function to run the Streamlit application."""
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Create Database", "Ask Question"])

    if page == "Create Database":
        create_database_page()
    elif page == "Ask Question":
        ask_question_page()


if __name__ == "__main__":
    main()
