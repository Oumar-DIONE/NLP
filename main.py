# Importing librairies

import argparse
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import config


# Définition de fonction
def encoder(data_set):
    # use LabelEncoder to replace purchased (dependent variable) with 0 and 1
    data_set["Email No."] = LabelEncoder().fit_transform(data_set["Email No."])
    y = data_set["Prediction"]
    x = data_set.drop(["Prediction"], axis=1)
    return x, y


def split_scale(x, y, test_size=0.3):
    # Splitting the dataset  into  training  and test set
    x, xt, y, yt = train_test_split(X, Y, test_size=test_size, random_state=0)
    # func returns train and test data. It takes dataset and
    # then split size test_size =0.3 means 30% data is for test and rest for training and random_state
    scaler = StandardScaler()
    x = scaler.fit_transform(x)  # apply on whole x data
    xt = scaler.transform(xt)
    return x, y, xt, yt


def knn_model(n_neighbors, x, y, p=2, metric_="minkowski"):

    model = KNeighborsClassifier(
        n_neighbors, p=p, metric=metric_
    )  # by default n_neighbors= 5
    model.fit(x, y)
    return model


def make_prediction(x, model):
    y = model.predict(x)
    return y


def evaluate(y1, y2):
    cm = confusion_matrix(y1, y2)
    accurace_ = accuracy_score(y1, y2)
    print(f"{accurace_:.1%} de bonnes réponses sur les données de test pour validation")
    print("les nombres de voisins plus proches  est ", args.n_neighbors)
    print("matrice de confusion")
    print(cm)


config = config.import_yaml_config()
DATA_PATH = config.get("data_path", "emails.csv")
# Parameter
parser = argparse.ArgumentParser(description="le nombre de voisins")
parser.add_argument(
    "--n_neighbors",
    type=int,
    default=5,
    help="un nombre de plus proche voisin à choisir",
)
args = parser.parse_args()


# Load Data
dataset = pd.read_csv(DATA_PATH)

categorical = [var for var in dataset.columns if dataset[var].dtype == "O"]
numerical = [var for var in dataset.columns if dataset[var].dtype != "O"]


# Data preprocessing

# dataset["Email No."] = LabelEncoder().fit_transform(dataset["Email No."])

X, Y = encoder(dataset)

x_train, y_train, x_test, y_test = split_scale(X, Y)

# Build model

classifier = knn_model(n_neighbors=args.n_neighbors, x=x_train, y=y_train)
# make prediction on test set

y_pred = make_prediction(x_test, classifier)

# Evaluate model

evaluate(y_test, y_pred)
