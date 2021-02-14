import numpy as np

def read_documents(file):
    labels = []
    docs = []
    txt = open(file, encoding='UTF=8')
    for i in txt.readlines():
        labels.append(i.lower().split()[:2])
        docs.append(i.lower().split()[2:])
    return docs, labels


all_docs, all_labels = read_documents('all_sentiment_shuffled.txt')
split_point = int(0.80*len(all_docs))
train_docs = all_docs[:split_point]
train_labels = all_labels[:split_point]
#the rest of 20%
eval_docs = all_docs[split_point:]
eval_labels = all_labels[split_point:]
print(train_labels)

