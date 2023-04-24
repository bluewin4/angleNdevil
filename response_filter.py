import random
import re
from typing import List

def remove_repetitive_phrases(text: str) -> str:
    """
    Remove repetitive phrases from the input text.

    Args:
        text (str): Input text with potential repetitive phrases.

    Returns:
        str: Text with repetitive phrases removed.
    """
    phrases = re.split(r'\s+', text)
    unique_phrases = []

    for phrase in phrases:
        if phrase not in unique_phrases:
            unique_phrases.append(phrase)

    return ' '.join(unique_phrases)

def improve_creativity(text: str, synonyms: List[str]) -> str:
    """
    Replace words in the input text with synonyms to improve creativity.

    Args:
        text (str): Input text to improve creativity.
        synonyms (List[str]): List of synonyms.

    Returns:
        str: Text with improved creativity.
    """
    words = text.split()
    creative_text = []

    for word in words:
        if random.random() < 0.5:
            synonym = random.choice(synonyms)
            creative_text.append(synonym)
        else:
            creative_text.append(word)

    return ' '.join(creative_text)

def filter_and_improve_responses(response: str, synonyms: List[str]) -> str:
    """
    Apply both removing repetitive phrases and improving creativity methods to the given response.

    Args:
        response (str): The initial response generated by the bot.
        synonyms (List[str]): List of synonyms.

    Returns:
        str: Improved response after applying both methods.
    """
    filtered_response = remove_repetitive_phrases(response)
    creative_response = improve_creativity(filtered_response, synonyms)

    return creative_response