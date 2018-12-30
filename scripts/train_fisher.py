import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
import pandas as pd
from sklearn.svm import NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from splitter import splitLabel, splitFV
import time
from sklearn.neighbors import KNeighborsClassifier
# input_filename_X = 'fisher_vectors_copy.csv'
# input_filename_Y = 'labels_copy.csv'

# train_X, valid_X, test_X = splitFV(input_filename_X, input_filename_Y)
# train_y, valid_y, test_y = splitLabel(input_filename_Y)

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

train_X = createMemFile(1952611,6400,"train_split.csv","trainMem_X.txt")
print('Done with train_X')
train_y = createMemFile(1952611,1,"train_label_split.csv","trainMem_Y.txt")
print('Done with train_y')
valid_X = createMemFile(100000,6400,"valid_split.csv","validMem_X.txt")
print('Done with valid_X')
valid_y = createMemFile(100000,1,"valid_label_split.csv","validMem_Y.txt")
print('Done with valid_y')
test_X = createMemFile(300000,6400,"test_split.csv","testMem_X.txt")
print('Done with test_X')
test_y = createMemFile(300000,1,"test_label_split.csv","testMem_Y.txt")
print('Done with test_y')

train_y = train_y.flatten()
valid_y = valid_y.flatten()
test_y = test_y.flatten()

# print(train_X)
# print(train_y)

time_init = time.time()
print("Training SGD")
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(train_X, train_y)
print("Validating SGD")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
print(time.time() - time_init)


time_init = time.time()
print("Training LogisticRegression")
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
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
print(time.time() - time_init)


time_init = time.time()
print("Training LinearSVC")
clf = SVC(kernel='linear')
clf.fit(train_X, train_y)
print("Validating LinearSVC")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
print(time.time() - time_init)


time_init = time.time()
print("Training RandomForestClassifier")
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train_X, train_y)
print("Validating RandomForestClassifier")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
print(time.time() - time_init)


time_init = time.time()
print("Training gaussian SVC")
clf = SVC(kernel='rbf') 
clf.fit(train_X, train_y)
print("Validating gaussian SVC")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
print(time.time() - time_init)


time_init = time.time()
print("Training sigmoid SVC")
clf = SVC(kernel='sigmoid')
clf.fit(train_X, train_y)
print("Validating sigmoid SVC")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
print(time.time() - time_init)

time_init = time.time()
print("Training K-NN")
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(train_X, train_y)
print("Validating K-NN")
y_hat = clf.predict(valid_X)
accuracy = accuracy_score(y_hat,valid_y)
print("Validation Data:")
print(accuracy)
y_hat = clf.predict(test_X)
accuracy = accuracy_score(y_hat,test_y)
print("Testing Data:")
print(accuracy)
print(time.time() - time_init)
