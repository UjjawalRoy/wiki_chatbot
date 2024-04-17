import random

from constants import chat_start_messages, chat_start_responses


def start_chat_responses(start_sequence):
    for word in start_sequence.split():
        if word.lower() in chat_start_messages:
            return random.choice(chat_start_responses)
