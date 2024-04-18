from ast import literal_eval

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from generate_output.constants import tokenized_sentences_filename, answer_not_found_message
from generate_output.preprocess import preprocess_data
from generate_output.qa_pipeline import start_chat_responses

vectorizer = TfidfVectorizer(tokenizer=preprocess_data, stop_words='english')

with open(tokenized_sentences_filename, 'r') as f:
    sentence_tokens = f.read()
    sentence_tokens = literal_eval(sentence_tokens)


def respond(user_query):
    ret, response = start_chat_responses(user_query)
    if ret:
        return response
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
