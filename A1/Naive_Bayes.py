import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB


def read_documents(file):
    labels = []
    docs = []
    txt = open(file, encoding='UTF=8')
    for i in txt.readlines():
        labels.append(i.lower().split()[:2])
        docs.append(i.lower().split()[2:])
    return docs, labels


def label_dist(all_labels):
    temp_dict = {}
    for i in all_labels:
        if i[0] not in temp_dict.keys():
            temp_dict[i[0]] = 1
        else:
            temp_dict[i[0]] += 1

    print(temp_dict)

    fig = plt.figure(figsize=(10, 7))
    labels = [i for i in temp_dict.keys()]
    values = [i for i in temp_dict.values()]
    plt.bar(labels, values)
    plt.show()


# Task 0
all_docs, all_labels = read_documents('all_sentiment_shuffled.txt')
split_point = int(0.80*len(all_docs))

# training 80%
train_docs = all_docs[:split_point]
train_labels = all_labels[:split_point]

# the rest of 20%
eval_docs = all_docs[split_point:]
eval_labels = all_labels[split_point:]


# Task 1
label_dist(all_labels)


# Task 2
bayes = GaussianNB()
