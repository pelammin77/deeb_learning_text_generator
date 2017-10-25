import numpy as np
import random
import tensorflow
import datetime

text = open('wiki.test.raw',encoding="utf8").read()
#print(len(text))
#print(text[:1000])


chars = sorted(list(set(text))) # get all chars into text and sorted
chars_size = len(chars)

#print("num of chars", len(chars))
#print('chars:', chars)



char_to_id = dict((c, i) for c, i in enumerate(chars))
id_to_char = dict((i, c) for i, c in enumerate(chars))


def sample(prediction):
    r = random.uniform(0,1) # generate random therhold value
    s = 0 # store char
    char_id = len(prediction) - 1
    for i in range(len(prediction)):
        s += prediction[i]
        if s >=r:
            char_id = i
            break
    char_one_hot = np.zeros(shape=[chars_size]) # generates binary code for word
                                                #exaple car = 01110 boat = 00110
    char_one_hot[char_id] = 1.0
    return char_one_hot

section_len = 50
skip =  2
sections = []
next_chars = []

for i in range(0, len(text)-section_len, skip): # take every two char
    sections.append(text[i: i+section_len]) # 50 chars
    next_chars.append(text[i + section_len]) # next 50 chars
