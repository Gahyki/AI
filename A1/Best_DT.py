from __future__ import division
from codecs import open

import nltk
from sklearn import tree, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from nltk.corpus import stopwords
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import time

start_time = time.time()
def read_documents(doc_file):
    docs = []
    labels = []
    with open(doc_file, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            docs.append(words[3:])
            labels.append(words[1])

    return docs, labels


def cleaning_docs(document):
    clean = []
    stop_words = set(stopwords.words('english'))
    for i in document:
        words = [word for word in i if word.isalpha()]
        words = [w for w in words if not w in stop_words]
        clean.append(words)
    return clean


def label_to_number(label):
    number_train_label = [0] * len(label)  # f(x)
    for i in range(len(label)):
        if train_labels[i] == 'neg':
            number_train_label[i] = 0
        else:  # the positive
            number_train_label[i] = 1
    return number_train_label



# task 0 reading the document and splitting the data
all_docs, all_labels = read_documents('all_sentiment_shuffled.txt')
output = open("best_dt.txt",'w')
split_point = int(0.80 * len(all_docs))
# training set
train_docs = all_docs[:split_point]  # X
train_labels = all_labels[:split_point]  # Y
# testing set
eval_docs = all_docs[split_point:]  # 2383
eval_labels = all_labels[split_point:]  # 2383

################## CLEANING DATA ##############
clean_train_docs = cleaning_docs(train_docs)
clean_eval_docs = cleaning_docs(eval_docs)
################## CLEANING DATA ##############

####### converting the pos and neg to numbers #######
train_labels_number = label_to_number(train_labels)

# Evalution labels configuration
eval_labels_number = [0] * 2383
for i in range(len(eval_labels)):
    if eval_labels[i] == 'neg':
        eval_labels_number[i] = 0
    else:
        eval_labels_number[i] = 1

########### TESTING HERE FOR NEW CLEAN TEXT ####################
docs_Results_Clean = [""] * 9531
for i in range(len(clean_train_docs)):
    docs_Results_Clean[i] = ' '.join(clean_train_docs[i])

eval_results_clean = [""] * 2383
for i in range(len(eval_docs)):
    eval_results_clean[i] = ' '.join(eval_docs[i])
########### TESTING HERE FOR NEW CLEAN TEXT ####################

vect = CountVectorizer()
vect.fit(docs_Results_Clean)
x_train = vect.transform(docs_Results_Clean)
x_test = vect.transform(eval_results_clean)
x_train1 = vect.transform()

# -------------- Random forest algorithm --------------------#
randF = RandomForestClassifier()
randF.fit(x_train, train_labels_number)
y_pred = randF.predict(x_test) # the prediction
# -------------- output printing --------------------#
output.write("****** Random forest results ******" + "\n")
output.write("Accuracy: " + str(metrics.accuracy_score(eval_labels_number, y_pred)) + "\n\n")
output.write("Confusion matrix:\n" + str(confusion_matrix(eval_labels_number, y_pred)) + "\n\n")
output.write(str(classification_report(eval_labels_number, y_pred)) + "\n")
# -------------- Classic decision Tree --------------------#
clf = DecisionTreeClassifier(splitter='random')
clf = clf.fit(x_train, train_labels_number)
y_pred1 = clf.predict(x_test)
review = ["I wanted to read this over the length of his presidency, but it never happened. It was a great read.Really helped me understand inner city life and the struggles of the black community.",
          "I bought this for my mom. She is loving it. Also it was delivered a day earlier than promised. Amazon Prime is great. Keep up the good work"]
x_train1 = vect.transform(review);
yy_test = clf.predict(x_train1)
# -------------- output printing --------------------#
output.write("****** classic decision tree results ******" + "\n")
output.write("Accuracy: " + str(metrics.accuracy_score(eval_labels_number, y_pred1)) + "\n\n")
output.write("Confusion matrix:\n" + str(confusion_matrix(eval_labels_number, y_pred1)) + "\n\n")
output.write(str(classification_report(eval_labels_number, y_pred1)) + "\n")
output.write("--- %s seconds ---" % (time.time() - start_time))

print(yy_test[0])