import re
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


def find_paragraphs(raw_data):
    """
    Find paragraphs in raw HTML data.

    Args:
        raw_data: BeautifulSoup object representing the raw HTML data.

    Returns:
        list: List of paragraphs found in the raw HTML data.
    """
    return raw_data.find_all('p')


def remove_unwanted_characters(input_str: str):
    """
    Remove unwanted characters from a string.

    Args:
        input_str (str): Input string containing unwanted characters.

    Returns:
        str: Cleaned string with unwanted characters removed.
    """
    pattern = re.compile(r'(\x1b\[([0-9;]+)m|\[\d+\])')
    clean_text = pattern.sub('', input_str)
    escape_pattern = re.compile(r'\n')
    clean_text = escape_pattern.sub(' ', clean_text)
    return clean_text


def remove_punctuations(input_str):
    """
    Remove punctuations from a string.

    Args:
        input_str (str): Input string containing punctuations.

    Returns:
        str: Cleaned string with punctuations removed.
    """
    pattern_punctuation = r'[^\w\s]'
    return re.sub(pattern_punctuation, '', input_str)


def tokenize_data(data):
    """
    Tokenize data into sentences and words.

    Args:
        data (str): Input string to be tokenized.

    Returns:
        tuple: Tuple containing tokenized sentences and tokenized words.
    """
    tokenized_sentences = nltk.sent_tokenize(data)
    tokenized_words = nltk.word_tokenize(data)
    return tokenized_sentences, tokenized_words


def lemmatize_text(tokens):
    """
    Lemmatize a list of tokens.

    Args:
        tokens (list): List of tokens to be lemmatized.

    Returns:
        list: List of lemmatized tokens.
    """
    lemmatized_token_list = []
    for token in tokens:
        lemmatized_token_list.append(lemmatizer.lemmatize(token))
    return lemmatized_token_list


def preprocess_data(input_string):
    """
    Preprocess input string by removing unwanted characters, punctuations, and lemmatizing tokens.

    Args:
        input_string (str): Input string to be preprocessed.

    Returns:
        list: List of lemmatized tokens.
    """
    input_string = input_string.encode('ascii', errors='ignore').decode("utf-8")
    input_string = remove_unwanted_characters(input_str=input_string)
    input_string = remove_punctuations(input_str=input_string).lower()
    _, tokenized_words = tokenize_data(data=input_string)
    lemmatized_tokens_list = lemmatize_text(tokenized_words)
    return lemmatized_tokens_list


def tokenize_sent(input_string):
    """
    Tokenize input string into sentences.

    Args:
        input_string (str): Input string to be tokenized.

    Returns:
        list: List of tokenized sentences.
    """
    input_string = input_string.encode('ascii', errors='ignore').decode("utf-8")
    input_string = remove_unwanted_characters(input_str=input_string)
    tokenized_sentences = nltk.sent_tokenize(input_string)
    return tokenized_sentences
