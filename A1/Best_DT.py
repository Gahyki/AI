from __future__ import division
from codecs import open
import numpy as np
import re
import heapq


def read_documents(doc_file):
    docs = []
    labels = []
    with open(doc_file,encoding='utf-8') as f:
        for line in f:
            words= line.strip().split()
            docs.append(words[3:])
            labels.append(words[1])

    return docs,labels


# task 0 reading the document and splitting the data

all_docs,all_labels = read_documents('all_sentiment_shuffled.txt')

split_point = int(0.80*len(all_docs))

# training set
train_docs = all_docs[:split_point] # X
train_labels = all_labels[:split_point] # Y
# testing set
eval_docs = all_docs[split_point:]
eval_labels = all_labels[split_point:]

# label is F(x)
# words are our instance

word_count = {}
for i in train_docs:
    for word in i:
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1

# wordcount lent 52392
numberofLabel = {}
for word in train_labels:
    if word not in numberofLabel.keys():
        numberofLabel[word] = 1
    else:
        numberofLabel[word] += 1

# 4684 neg and 4847 pos


X = []
for i in train_docs:
    Vector = []
    for word in word_count:
        if word in i:
            Vector.append(1)
        else:
            Vector.append(0)
    X.append(Vector)

X = np.asarray(X)

print(X)

