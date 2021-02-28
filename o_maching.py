from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)

print(iris.target)

print(iris.target_names)

print(iris.data.shape)

print(iris.target.shape)

# ---------------------------------------------------------------

# Importing KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

X = iris.data
y = iris.target

knn.fit(X,y)

print(knn.predict( [ [5.1,3.5,1.4,0.2] ] ))

print(knn.predict( [ [5.9,3,5.1,1.8] ] ))

# ---------------------------------------------------------------

#Separate Data into Train and Test groups
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=20)

print(X_test.shape)

knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(predictions)

print(y_test)

from sklearn import metrics 
performance = metrics.accuracy_score(y_test, predictions)
print(performance)

# ---------------------------------------------------------------

# Excercise - Finding the best value of K
k_values= {}
k = 1 

while k <=25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    performance = metrics.accuracy_score(y_test, predictions)
    k_values[k] = round(performance, 4)
    k +=1
print(k_values)

import matplotlib.pyplot as plt
%matplotlib inline 
#Search for what

plt.plot(list(k_values.keys()), list(k_values.values()))
plt.xlabel("Values of K")
plt.ylabel("Performance")
plt.show()

# ---------------------------------------------------------------

# Logistic Regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
#print(logreg.predict_proba( [ [6.7,3.3,5.7,2.5] ] ))
predictions_logreg = logreg.predict(X_test)
performance_logreg = metrics.accuracy_score(y_test, predictions_logreg)
print(performance_logreg)