import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
import sklearn.multiclass
import sklearn.model_selection
import sklearn.linear_model
from sklearn.datasets import fetch_openml

trafficSigns = fetch_openml("GTSRB-HueHist")

X = trafficSigns.data
Y = trafficSigns.target

X_train, X_test, Y_train, Y_test = sk.model_selection.train_test_split(X, Y, train_size=0.8)

model = sk.multiclass.OneVsRestClassifier(sk.linear_model.LogisticRegression(solver="newton-cg",tol=0.1))
model.fit(X_train/255.0, Y_train)

print(sk.metrics.accuracy_score(Y_test, model.predict(X_test/255.0)))