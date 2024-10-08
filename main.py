""" package docstrings """
# /home/headless/work/NLP
# Importing librairies

import sys
import os
import argparse

# Ajouter le chemin du dossier 'src/data' dans sys.path
# Ajouter le chemin du dossier 'src' dans sys.path
sys.path.append(os.path.abspath("src"))

import train_evaluate
import build_features
import import_data
# Parameter
parser = argparse.ArgumentParser(description="le nombre de voisins")
parser.add_argument(
    "--n_neighbors",
    type=int,
    default=5,
    help="un nombre de plus proche voisin à choisir",
)
args = parser.parse_args()
CONFIG_PATH = "/home/onyxia/work/classification_K_Nearest_Neighbour/configuration/config.yaml"
CONFIG_PATH = "/home/headless/work/NLP/config.yaml"

# Load Data
dataset = import_data.load_data(CONFIG_PATH)

categorical = [var for var in dataset.columns if dataset[var].dtype == "O"]
numerical = [var for var in dataset.columns if dataset[var].dtype != "O"]


# Data preprocessing

# dataset["Email No."] = LabelEncoder().fit_transform(dataset["Email No."])

X, Y = build_features.encoder(dataset)

x_train, y_train, x_test, y_test = build_features.split_scale(X, Y)
# Sauvegarder le DataFrame dans un fichier CSV
FILE1 = "/home/onyxia/work/classification_K_Nearest_Neighbour/data/derived/X.csv"
FILE2 = "/home/onyxia/work/classification_K_Nearest_Neighbour/data/derived/y.csv"
# Sauvegarder le DataFrame dans un fichier CSV
FILE1 = "/home/headless/work/NLP/data/derived/X.csv"
FILE2 = "/home/headless/work/NLP/data/derived/y.csv"
X.to_csv(FILE1, index=False, encoding='utf-8')
Y.to_csv(FILE2, index=False, encoding='utf-8')

print("Le fichier CSV a été sauvegardé avec succès.")
# Build model

classifier = train_evaluate.knn_model(
    n_neighbors=args.n_neighbors, x=x_train, y=y_train)
# make prediction on test set

y_pred = train_evaluate.make_prediction(x_test, classifier)

# Evaluate model
print("les nombres de voisins plus proches  est ", args.n_neighbors)
train_evaluate.evaluate(y_test, y_pred)
