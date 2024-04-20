# Wikipedia Chatbot


## What is Wikipedia chatbot?

This Wikipedia chatbot is based on a relevant information retrieval system. It utilizes seq2seq vectorizer 
for semantic search and
TF-IDF vectorizer for information retrieval
to embed the data scraped from Wikipedia. Subsequently, it can answer users' queries by retrieving relevant information 
from the Wikipedia dataset.

## How to Install

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/wikipedia-chatbot.git
    ```

2. Navigate to the project directory:

    ```
    cd wikipedia-chatbot
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Run the backend server:

    ```
    python main.py
    ```

5. Run the frontend:

    ```
    streamlit run frontend.py
    ```

## Usage

1. In the Streamlit app, click on the "Create Database" tab.
2. Choose the type of database you want to create.
3. Delete the chromadb folder under the databases directory first before creating a new database.
4. Paste the URL of the Wikipedia page you want to use and click "Submit".
5. Once submitted, navigate to the "Ask Question" tab.
6. Make sure if 'Vector database' was not chosen earlier, navigate to main.py and set semantic_query=False in the 
   'ask_question' function.
7. Use the chatbot to ask questions related to the Wikipedia page you previously stored in the database.

Enjoy querying the Wikipedia chatbot for relevant information!

## References

- https://github.com/RajkumarGalaxy/Wiki-IR-ChatBot
- https://youtu.be/sBhK-2K9bUc?si=onKci3aW0q1NkAUA
- https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
- https://realpython.com/chromadb-vector-database/#meet-chromadb-for-llm-applications