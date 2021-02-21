import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import time
start_time = time.time()

def read_documents(file):
    # Custom read documents
    labels = []
    docs = []
    txt = open(file, encoding='UTF=8')
    for i in txt.readlines():
        labels.append(i.lower().split()[1])
        docs.append(i.lower().split(" ")[3:])
    return docs, labels


def label_dist(labels):
    # Distribution of positives and negatives plotted out on graph
    temp_dict = {}
    for i in labels:
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


def matrixbuilder(docs):
    # 8 000 rows by 40 000 columns
    # Get a dictionary with all possible keys
    keys = {}
    for sample in docs:
        for word in sample:
            keys[word] = 0
    # Create a matrix with
    matrix = []
    for i in docs:
        temp = keys.copy()
        for j in i:
            temp[j] += 1
        matrix.append(list(temp.values()))
    return matrix


# Creating txt file
output = open("naive_bayes-all_sentiment_shuffled.txt", "w")

# Task 0
docs, all_labels = read_documents('all_sentiment_shuffled.txt')
all_docs = matrixbuilder(docs)
split_point = int(0.80*len(all_docs))

# training 80%
train_docs = all_docs[:split_point]
train_labels = all_labels[:split_point]

# the rest of 20%
eval_docs = all_docs[split_point:]
eval_labels = all_labels[split_point:]


# Task 1
# Plotting the labels
label_dist(all_labels)


# Task 2
bayes = GaussianNB()

pred_labels = bayes.fit(train_docs, train_labels).predict(eval_docs)


# Task 3
output.write("Accuracy: " + str(accuracy_score(eval_labels, pred_labels)) + "\n\n")
output.write("Confusion matrix:\n" + str(confusion_matrix(eval_labels, pred_labels)) + "\n\n")
output.write(str(classification_report(eval_labels, pred_labels)) + "\n")
output.write("--- %s seconds ---" % (time.time() - start_time))


# Task 4
# There is no weight associated in positive words.
for i, j, k in zip(eval_labels[:10], pred_labels[:10], docs[int(0.80*len(all_docs)):int(0.80*len(all_docs))+11]):
    print("Eval: " + str(i) + "\t" + str(k))
    print("Pred: " + str(j) + "\n")
