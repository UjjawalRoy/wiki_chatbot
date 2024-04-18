import os

from generate_output.constants import lemmatized_words_list_filename, tokenized_sentences_filename
from generate_output.preprocess import preprocess_data


def dump_db(data, input_string):
    if not os.path.exists(lemmatized_words_list_filename):
        with open(lemmatized_words_list_filename, 'w'):
            pass
    if not os.path.exists(tokenized_sentences_filename):
        with open(tokenized_sentences_filename, 'w'):
            pass

    lemmatized_tokens_list, tokenized_sentences = preprocess_data(data=data, input_string=input_string)

    with open(lemmatized_words_list_filename, 'w') as file:
        # Write the text to the file
        file.write(str(lemmatized_tokens_list))

    with open(tokenized_sentences_filename, 'w') as file:
        # Write the text to the file
        file.write(str(tokenized_sentences))

    return "Database successfully created"
