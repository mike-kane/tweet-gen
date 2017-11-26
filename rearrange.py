import random
import sys

def rearrange(input_words):
    '''
    Takes a list of words, rearranges them, and returns a new string.
    '''
    output_string = ""
    # Loop ends when all words have been popped out of word_list
    while len(input_words) != 0:
        word = random.choice(input_words)
        input_words.remove(word)
        output_string += word + " "
    return output_string


if __name__ == "__main__":
    input_string = sys.argv[1:]
    print(input_string)
    print(rearrange(input_string))
