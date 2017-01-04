import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

X, y = np.arange(10).reshape((5, 2)), range(5)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# iris = datasets.load_iris()

l1 = []
for i in range(10):
    l1.append(i)

import heapq

print(heapq.nlargest(5, l1))
