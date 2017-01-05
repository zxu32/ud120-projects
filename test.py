import numpy as np
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), range(5)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

import heapq

print(heapq.nlargest(2, [(1,2),(3,4),(5,2),(6,7)], key=lambda i: i[1]))
