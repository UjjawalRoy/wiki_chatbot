import os

import nltk
from nltk.stem import WordNetLemmatizer
import re
from constants import lemmatized_words_list_filename, tokenized_sentences_filename

lemattizer = WordNetLemmatizer()


def find_paragraphs(raw_data):
    return raw_data.find_all('p')


def remove_unwanted_characters(input_str):
    pattern = r'\[\d+\]|\[\d+\.\d+\]|\\[nrt]'
    return re.sub(pattern, ' ', input_str)


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


