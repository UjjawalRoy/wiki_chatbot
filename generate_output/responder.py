import ast

from sklearn.feature_extraction.text import TfidfVectorizer

from generate_output.preprocess import lemmatize_text, preprocess_data
from generate_output.constants import lemmatized_words_list_filename, tokenized_sentences_filename

vectorizer = TfidfVectorizer(tokenizer=preprocess_data, stop_words='english')

with open(tokenized_sentences_filename, 'r') as f:
    sentence_tokens = f.read()
    sentence_tokens = ast.literal_eval(sentence_tokens)

def repond(user_query):
    word_vectors = vectorizer.fit_transform()
