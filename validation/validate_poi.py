#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
     features, labels, test_size=0.3, random_state=42)

### it's all yours from here forward!

print type(features_train)
print type(features_test)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
#print clf.score(features_test, labels_test)
#print clf

pred = clf.predict(features_test)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print 'the precision score is ', precision_score(labels_test, pred)
print 'the recall score is ', recall_score(labels_test, pred)


#print labels_test

from sklearn.metrics import confusion_matrix
a = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
b = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print 'the precision score is ', precision_score(b, a)
print 'the recall score is ', recall_score(b,a)

print confusion_matrix(b, a)
#print clf.predict(features_test).tolist().count(1.)