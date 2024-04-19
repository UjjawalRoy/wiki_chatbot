import random
from generate_output.constants import chat_start_messages, chat_start_responses, chat_end_messages, chat_end_responses


def start_chat_responses(start_sequence):
    """
    Determine if the start sequence matches any predefined chat start messages.

    Args:
        start_sequence (str): The sequence to check.

    Returns:
        tuple: A tuple containing a boolean indicating if the start sequence matches any predefined chat start messages,
               and a response message.
    """
    for word in start_sequence.split():
        if word.lower() in chat_start_messages:
            return True, random.choice(chat_start_responses)
        else:
            return False, start_sequence


def end_chat_responses(end_sequence):
    """
    Determine if the end sequence matches any predefined chat end messages.

    Args:
        end_sequence (str): The sequence to check.

    Returns:
        tuple: A tuple containing a boolean indicating if the end sequence matches any predefined chat end messages,
               and a response message.
    """
    for word in end_sequence.split():
        if word.lower() in chat_end_messages:
            return True, random.choice(chat_end_responses)
        else:
            return False, end_sequence
