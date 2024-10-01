# Importing librairies

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Load Data
dataset = pd.read_csv("emails.csv")

categorical = [var for var in dataset.columns if dataset[var].dtype == "O"]
numerical = [var for var in dataset.columns if dataset[var].dtype != "O"]


# Data preprocessing
# use LabelEncoder to replace purchased (dependent variable) with 0 and 1
dataset["Email No."] = LabelEncoder().fit_transform(dataset["Email No."])
y = dataset["Prediction"]
x = dataset.drop(["Prediction"], axis=1)

# Splitting the dataset  into  training  and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# func returns train and test data. It takes dataset and
# then split size test_size =0.3 means 30% data is for test and rest for training and random_state
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)  # apply on whole x data
x_test = scaler.transform(x_test)

# Build model
classifier = KNeighborsClassifier(
    n_neighbors=2, p=2, metric="minkowski"
)  # by default n_neighbors= 5
classifier.fit(x_train, y_train)
# make prediction on test set
y_pred = classifier.predict(x_test)

# Evaluate model
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
accurace_ = accuracy_score(y_test, y_pred)
print(f"{accurace_:.1%} de bonnes réponses sur les données de test pour validation")
print(20 * "-")
print("matrice de confusion")
print(cm)
