import json

import streamlit as st
import requests


def create_database_page():
    st.title("Create Database")
    url = st.text_input("Enter URL")
    if st.button("Submit"):
        response = requests.post("http://localhost:8001/createdb", json={"url": url})
        if response.status_code == 200:
            st.success("Database created successfully")
        else:
            st.error("Error creating database")


def ask_question_page():
    st.title("Ask Question")
    question = st.text_input("Enter your question")
    if st.button("Ask"):
        response = requests.post("http://localhost:8001/ask", data=json.dumps({"query": question.lower()}))
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
