import json
from nltk_utils import tokennize, stem, bag_of_words

with open('intents.json') as f:
    intents =  json.load(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokennize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ','] 
print(all_words)