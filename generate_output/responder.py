from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from generate_output.preprocess import preprocess_data, find_paragraphs, remove_unwanted_characters, \
    remove_punctuations, tokenize_data, lemmatize_text

vectorizer = TfidfVectorizer(tokenizer=preprocess_data, stop_words='english')

def preprocess_data(data, input_string):
    paragraphs = find_paragraphs(raw_data=data)
    input_string += paragraphs.text
    input_string = remove_unwanted_characters(input_str=input_string)
    input_string = remove_punctuations(input_str=input_string).lower()
    tokenized_sentences, tokenized_words = tokenize_data(data=input_string)
    lemmatized_tokens_list = lemmatize_text(tokenized_words)
    return lemmatized_tokens_list, tokenized_sentences

def repond(user_query):
    word_vectors = vectorizer.fit_transform()