import re


def count_words(sentence):
    words = re.findall(r'[a-z0-9]+(?:\'?[a-z0-9]+)?', sentence, re.I)

    words_count = {}
    for word in words:
        words_count[word.lower()] = words_count.get(word.lower(), 0) + 1

    return words_count