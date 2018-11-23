import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import  matplotlib,
import scipy,  sklearn, pytest,  unittest
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
# use scipy, use pytest, use unittest

def dataload_fun( filename ,rowput):
    print("Start Data load")
    fdataset = pd.read_csv(filename) #, names=names, skiprows=[0])
    print(fdataset.size)
    print("Image data Shape", fdataset.shape)
    print(fdataset.head(rowput))
    print("End data load")
    return fdataset, fdataset.shape[1]

def do_test_train_split(indataset, inheaderlen):
    print("BEGIN Create train test split")
    X = indataset.iloc[:, :-1].values
    y = indataset.iloc[:, inheaderlen - 1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    print("END Create train test split")
    return X_train, X_test, y_train, y_test

def do_feature_scaling(xtrain, xtest):
    print("BEGIN Feature scaling")
    scaler = StandardScaler()
    scaler.fit(xtrain)
    X_train = scaler.transform(xtrain)
    X_test = scaler.transform(xtest)
    print("END Feature scaling")
    return X_train, X_test

def create_KNN_classifier_prediction(xtst, xtr, ytra,neighbors):
    print("BEGIN training using KNN")
    clssf = KNeighborsClassifier(n_neighbors=neighbors)
    clssf.fit(xtr, ytra)
    print("END training using KNN")
    print("BEGIN predictions using KNN")
    ypred = clssf.predict(xtst)
    print("END predictions using KNN")
    return clssf, ypred

def calculate_error_output_knn_error_report(xtr, ytr, xtst, ytst):
    error = []
    print("BEGIN calculate mean error report  using KNN")
    # Calculating error for K values between 1 and 40
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(xtr, ytr)
        pred_i = knn.predict(xtst)
        error.append(np.mean(pred_i != ytst))
    print("END calculate mean error report  using KNN")

    print("BEGIN plot mean error report  using KNN")
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
             markerfacecolor='blue', markersize=10)
    plt.title('Error Rate K Value')
    plt.xlabel('K Value')
    plt.ylabel('Mean Error')
    print("END plot mean error report  using KNN")
    plt.show()

def main():
    UNANIMITY = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_unanimity.csv"
    VARIETY = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_variety.csv"
    DATALOAD_ROWPUT = 5
    NEIGHBORS = 10
    url = VARIETY


    dataset, headerlen = dataload_fun(url,DATALOAD_ROWPUT)
    X_train, X_test, y_train, y_test = do_test_train_split(dataset, headerlen)
    X_train, X_test = do_feature_scaling(X_train, X_test)
    classifier, y_pred = create_KNN_classifier_prediction(X_test,X_train,y_train,NEIGHBORS)

    print("END confusion matrix using KNN")
    print(confusion_matrix(y_test, y_pred))
    print("END confusion matrix using KNN")
    print("BEGIN classification report  using KNN")
    print(classification_report(y_test, y_pred))
    print("END classification report  using KNN")
    calculate_error_output_knn_error_report(X_train,y_train,X_test,y_test)

if __name__== "__main__":
  main()

