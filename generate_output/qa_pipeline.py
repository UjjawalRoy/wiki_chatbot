import random

from generate_output.constants import chat_start_messages, chat_start_responses, chat_end_messages, chat_end_responses


def start_chat_responses(start_sequence):
    for word in start_sequence.split():
        if word.lower() in chat_start_messages:
            return True, random.choice(chat_start_responses)
        else:
            return False, start_sequence


def end_chat_responses(end_sequence):
    for word in end_sequence.split():
        if word.lower() in chat_end_messages:
            return True, random.choice(chat_end_responses)
        else:
            return False, end_sequence
