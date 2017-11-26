import random
import sys

def generate_sentence(sentence_length=None):
    '''
    Generates a random sentence of words from /usr/share/dict/words.

    User may pass in an integer to determine how long the sentence should be.  If
    sentence_length is None, picks a random integer between 4 and 30 for sentence length instead.

    Returns the random sentence as a string.
    '''
    if not sentence_length:
        sentence_length = random.randint(4, 30)
    with open('/usr/share/dict/words', 'r') as f:
        corpus = []
        for line in f:
            corpus.append(line.rstrip())
    sentence = ''
    counter = 0
    while counter != sentence_length:
        sentence += random.choice(corpus) + " "
        counter += 1

    return sentence

if __name__ == '__main__':
    print(generate_sentence())
