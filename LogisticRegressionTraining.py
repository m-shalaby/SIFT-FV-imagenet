import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
import pandas as pd
from sklearn.svm import NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

import time
def createMemFile(shapeX,shapeY,fileNameIn,fileNameOut):
    aMemFile = np.memmap(fileNameOut, dtype='float32', mode='w+', shape=(shapeX,shapeY))
    n = 0
    i=0
    for chunk in pd.read_csv(fileNameIn, chunksize=10000):
        print(i)
        aMemFile[n:n+chunk.shape[0]] = chunk.values
        n += chunk.shape[0]
        i=i+1
    return aMemFile;aMemFile

train_X = createMemFile(195261,6400,"train_split.csv","trainMem_X.txt")
print('Done with train_X')
train_y = createMemFile(195261,1,"train_label_split.csv","trainMem_Y.txt")
print('Done with train_y')
valid_X = createMemFile(10000,6400,"valid_split.csv","validMem_X.txt")
print('Done with valid_X')
valid_y = createMemFile(10000,1,"valid_label_split.csv","validMem_Y.txt")
print('Done with valid_y')
test_X = createMemFile(30000,6400,"test_split.csv","testMem_X.txt")
print('Done with test_X')
test_y = createMemFile(30000,1,"test_label_split.csv","testMem_Y.txt")
print('Done with test_y')

train_y = train_y.flatten()
valid_y = valid_y.flatten()
test_y = test_y.flatten()


print("Training LogisticRegression: 100")
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial', C = 100)
clf.fit(train_X, train_y)
print("Validating LogisticRegression")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)


print("Training LogisticRegression: 200")
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial', C = 200)
clf.fit(train_X, train_y)
print("Validating LogisticRegression")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
