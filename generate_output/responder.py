from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from generate_output.constants import answer_not_found_message
from utils.constants import tokenized_sentences_filename, collection_name
from generate_output.preprocess import preprocess_data
from generate_output.qa_pipeline import start_chat_responses, end_chat_responses
from utils.create_vector_database import vector_db_client, embedding_func

vectorizer = TfidfVectorizer(tokenizer=preprocess_data, stop_words='english')
with open(tokenized_sentences_filename, 'r') as f:
    sentence_tokens = f.read()
    sentence_tokens = literal_eval(sentence_tokens)


def respond(user_query):
    """
    Generate a response to the user query.

    Args:
        user_query (str): The user's query.

    Returns:
        str: The response to the user's query.
    """
    start, start_response = start_chat_responses(user_query)
    end, end_response = end_chat_responses(user_query)
    if start:
        return start_response
    if end:
        return end_response
    sentence_tokens.append(user_query)
    sentence_vecs = vectorizer.fit_transform(sentence_tokens)
    score = cosine_similarity(sentence_vecs[-1], sentence_vecs)
    highest_scores_index = score.argsort()[0][-2]
    score = score.flatten()
    score.sort()
    val = score[-2]
    print(val)
    if val > 0.0:
        answer = sentence_tokens[highest_scores_index]
        sentence_tokens.pop()
        return answer
    else:
        sentence_tokens.pop()
        return answer_not_found_message


def semantic_responder(user_query):
    collection = vector_db_client.get_collection(name=collection_name, embedding_function=embedding_func)
    query_results = collection.query(query_texts=[user_query], n_results=1)
    return query_results['documents'][0][0]
