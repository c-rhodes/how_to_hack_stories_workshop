#!/usr/bin/env python3
import random 


def generate_sentence(sentence):
    """
        Given a sentence randomly produce
        a sentence of equal length.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    new_sentence = []
    for i in sentence:
        # iterate len(sentence) times and produce 
        # a new sentence of the same length
        new_sentence.append(random.choice(alphabet))
    
    new_sentence = ''.join(new_sentence) # list to string

    return new_sentence


def similarity(sentence, new_sentence):
    similarity = 0 # counter for characters that are at the same position in both sentences
    for character_position in range(len(sentence)):
        if sentence[character_position] == new_sentence[character_position]:
            similarity = similarity + 1

    percent_similarity = similarity / len(sentence) # % similarity
    return percent_similarity


def main():
    print('enter a starting sentence: ', end='')
    sentence = input()
    print()
    greatest_similarity_percent = 0   # % similarity of the most similar sentence
    greatest_similarity_sentence = '' # sentence that has the greatest % similarity to inputted sentence
    sentences_generated = 0           # # of sentences generated

    while True:
        new_sentence = generate_sentence(sentence) # generate new sentence
        percent_similarity = similarity(sentence, new_sentence) # % similarity of sentences
        if percent_similarity > greatest_similarity_percent:
            greatest_similarity_percent = percent_similarity
            greatest_similarity_sentence = new_sentence
        if sentences_generated % 200000 == 0 and sentences_generated != 0:
            # Give statistics every 200000 sentences
            print('Sentence of greatest similarity thus far: %s' %
                    greatest_similarity_sentence)
            print('Percentage similarity: %.2f' % 
                    greatest_similarity_percent)
            print('# of sentences generated: %d' % sentences_generated)
            print()

        sentences_generated = sentences_generated + 1

if __name__ == '__main__':
    main()
