from random import choice

def get_words(k):
    words = []
    with open('words.txt', 'r') as f:
        all_words = f.readlines()

        for _ in range(100):
            word = choice(all_words)
            words.append(word)
    return words
