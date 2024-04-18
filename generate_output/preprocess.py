import re

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemattizer = WordNetLemmatizer()


def find_paragraphs(raw_data):
    return raw_data.find_all('p')


def remove_unwanted_characters(input_str: str):
    pattern = re.compile(r'(\x1b\[([0-9;]+)m|\[\d+\])')
    clean_text = pattern.sub('', input_str)
    escape_pattern = re.compile(r'\n')
    clean_text = escape_pattern.sub(' ', clean_text)
    return clean_text


def remove_punctuations(input_str):
    pattern_punctuation = r'[^\w\s]'
    return re.sub(pattern_punctuation, '', input_str)


def tokenize_data(data):
    tokenized_sentences = nltk.sent_tokenize(data)
    tokenized_words = nltk.word_tokenize(data)
    return tokenized_sentences, tokenized_words


def lemmatize_text(tokens):
    lemmatized_token_list = []
    for token in tokens:
        lemmatized_token_list.append(lemattizer.lemmatize(token))
    return lemmatized_token_list


def preprocess_data(input_string):
    input_string = input_string.encode('ascii', errors='ignore').decode("utf-8")
    input_string = remove_unwanted_characters(input_str=input_string)
    input_string = remove_punctuations(input_str=input_string).lower()
    _, tokenized_words = tokenize_data(data=input_string)
    lemmatized_tokens_list = lemmatize_text(tokenized_words)
    return lemmatized_tokens_list


def tokenize_sent(input_string):
    input_string = input_string.encode('ascii', errors='ignore').decode("utf-8")
    input_string = remove_unwanted_characters(input_str=input_string)
    tokenized_sentences = nltk.sent_tokenize(input_string)
    return tokenized_sentences
