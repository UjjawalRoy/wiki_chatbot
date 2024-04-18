import json

import streamlit as st
import requests

import demo_questions


def create_database_page():
    st.title("Create Database")
    url = st.text_input("Enter Wiki URL")
    if st.button("Submit"):
        response = requests.post("http://localhost:8001/createdb", json={"url": url})
        if response.status_code == 200:
            st.success("Database created successfully")
        else:
            st.error("Error creating database")


def ask_question_page():
    st.title("Wikipedia Chatbot")
    query = st.selectbox("Select a question", ["What is artificial intelligence?",
                                               "Where is AI technology used?",
                                               "Which applications make use of advance AI?",
                                               "Who was the first person to conduct substantial research on AI?",
                                               "What are knowledge representation and knowledge engineering?",
                                               "What is a knowledge base?",
                                               "What is a rational 'Agent'?"])
    st.text('Or')
    question = st.text_input("Enter your question")
    if st.button("Ask"):
        response = ''
        if question:
            response = requests.post("http://localhost:8001/ask", data=json.dumps({"query": question.lower()}))
        else:
            response = requests.post("http://localhost:8001/ask", data=json.dumps({"query": query.lower()}))
        if response.status_code == 200:
            st.success("Answer: " + response.json())
        else:
            st.error("Error asking question")


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Create Database", "Ask Question"])

    if page == "Create Database":
        create_database_page()
    elif page == "Ask Question":
        ask_question_page()


if __name__ == "__main__":
    main()
