import os
from utils.constants import lemmatized_words_list_filename, tokenized_sentences_filename
from generate_output.preprocess import preprocess_data, tokenize_sent
from utils.constants import db_creation_success_message


def dump_db(data):
    """
    Dump the database with preprocessed data.

    Args:
        data (str): The input data to be dumped into the database.

    Returns:
        str: A success message indicating that the database was created successfully.
    """
    if not os.path.exists(lemmatized_words_list_filename):
        with open(lemmatized_words_list_filename, 'w'):
            pass
    if not os.path.exists(tokenized_sentences_filename):
        with open(tokenized_sentences_filename, 'w'):
            pass

    lemmatized_tokens_list = preprocess_data(input_string=data)
    tokenized_sentences = tokenize_sent(input_string=data)

    with open(lemmatized_words_list_filename, 'w') as file:
        file.write(str(lemmatized_tokens_list))

    with open(tokenized_sentences_filename, 'w') as file:
        file.write(str(tokenized_sentences))

    return db_creation_success_message
