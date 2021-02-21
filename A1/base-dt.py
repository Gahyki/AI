from __future__ import division
from codecs import open
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

output = open("Base_DT-dataset.txt", "w")

def read_documents(file):
    labels = []
    docs = []
    txt = open(file, encoding='UTF=8')
    for i in txt.readlines():
        labels.append(i.lower().split()[1])
        docs.append(i.lower().split()[3:])
    return docs, labels

def int_label(label):
    num_label = [0] * len(label)
    for i in range(len(label)):
        if train_labels[i] == 'neg':
            num_label[i] = 0
        else:
            num_label[i] = 1
    return num_label


all_docs, all_labels = read_documents('all_sentiment_shuffled.txt') #x, y
split_point = int(0.80*len(all_docs))

# training set 80%
train_docs = all_docs[:split_point] #X
train_labels = all_labels[:split_point] #Y

# testing set 20%
eval_docs = all_docs[split_point:]
eval_labels = all_labels[split_point:]
int_train_label = int_label(train_labels) #neg and pos to int values for fit method
#eval_labels_int = int_label(eval_labels)

eval_labels_int = [0] * 2383
for i in range(len(eval_labels)):
    if eval_labels[i] == 'neg':
        eval_labels_int[i] = 0
    else:
        eval_labels_int[i] = 1

count_vect = CountVectorizer(analyzer=lambda x: x)
X_vectorized = count_vect.fit_transform(all_docs)
X_train = count_vect.transform(train_docs)
x_test = count_vect.transform(eval_docs)

baseDT = DecisionTreeClassifier(criterion='entropy')
baseDT.fit(X_train, int_train_label) #change to int for train label
baseDT_pred = baseDT.predict(x_test)

output.write("Accuracy: " + str(metrics.accuracy_score(eval_labels_int, baseDT_pred)) + "\n\n")
output.write("Classification \n" + str(classification_report(eval_labels_int, baseDT_pred)) + "\n")
output.write("Confusion matrix:\n")
output.write(str(confusion_matrix(eval_labels_int, baseDT_pred)))


