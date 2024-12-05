""" package docstrings """
# /home/headless/work/NLP
# Importing librairies
# pylint: disable=wrong-import-position

import sys
import os
import argparse
from dotenv import load_dotenv
import pandas as pd
import joblib


# Ajouter le chemin du dossier 'src/data' dans sys.path
# Ajouter le chemin du dossier 'src' dans sys.path

sys.path.append(os.path.abspath("src/models"))
sys.path.append(os.path.abspath("src/data"))
sys.path.append(os.path.abspath("src/pipeline"))


# pylint: enable=wrong-import-position

import train_evaluate  # pylint: disable=E0401
import build_features  # pylint: disable=E0401
import import_data     # pylint: disable=E0401
# Parameter
parser = argparse.ArgumentParser(description="le nombre de voisins")
parser.add_argument(
    "--n_neighbors",
    type=int,
    default=5,
    help="un nombre de plus proche voisin à choisir",
)
args = parser.parse_args()

# Charger les variables d'environnement à partir du fichier .env (si utilisé)
load_dotenv(dotenv_path=".env")

# Chemin vers le répertoire du projet
project_root = os.path.dirname(os.path.abspath(__file__))

# Récupérer et construire des chemins
DATA_PATH = os.path.join(project_root, os.getenv("DATA_PATH"))
CONFIG_PATH = os.path.join(project_root, os.getenv("CONFIG_PATH"))
OUTPUT_X_PATH = os.path.join(project_root, os.getenv("OUTPUT_X_PATH"))
OUTPUT_Y_PATH = os.path.join(project_root, os.getenv("OUTPUT_Y_PATH"))
OUTPUT_accuracy = os.path.join(project_root, os.getenv("OUTPUT_accuracy"))
# Exemple d'utilisation
print("Data path:", DATA_PATH)
print("Config CONFIG_PATH:", CONFIG_PATH)
print("Config CONFIG_PATH:", OUTPUT_accuracy)
print(project_root)

# Load Data
#dataset = import_data.load_data(CONFIG_PATH, DATA_PATH)
# vider le contenu de la table emails qui est locument inutiles
# car on a les données dans datasets (temporairement et c'est suffisants).
#dataset=pd.read_csv(project_root+'/'+DATA_PATH)
dataset=pd.read_csv(DATA_PATH)
#import_data.truncate_table(DATA_PATH)

categorical = [var for var in dataset.columns if dataset[var].dtype == "O"]
numerical = [var for var in dataset.columns if dataset[var].dtype != "O"]


# Data preprocessing

# dataset["Email No."] = LabelEncoder().fit_transform(dataset["Email No."])

X, Y = build_features.encoder(dataset)
# Sauvegarder les données transfomées par l'étape  de préprocessing 
X.to_csv(OUTPUT_X_PATH, index=False, encoding='utf-8')
Y.to_csv(OUTPUT_Y_PATH, index=False, encoding='utf-8')
x_train, y_train, x_test, y_test = build_features.split_scale(X, Y)



print("Le fichier CSV a été sauvegardé avec succès.")
# Envoyer les données transfomées dans mon buckets S3 puis vider localement ces dataframes 
BUCKET_NAME = os.getenv('BUCKET_NAME')
#import_data.save_data_in_s3(CONFIG_PATH, OUTPUT_X_PATH, path_in_s3="EMAIL_DATA/X.csv")
#import_data.save_data_in_s3(CONFIG_PATH, OUTPUT_Y_PATH, path_in_s3="EMAIL_DATA/Y.csv")# Build model
# Vider les deux tables qui viennent d'être envoyées dans le bucket distant
import_data.truncate_table(OUTPUT_X_PATH)
import_data.truncate_table(OUTPUT_Y_PATH)

classifier = train_evaluate.knn_model(
    n_neighbors=args.n_neighbors, x=x_train, y=y_train)
# make prediction on test set
classifier = train_evaluate.knn_model(
    n_neighbors=args.n_neighbors, x=x_train, y=y_train)
# Sauvegarder le modèle sous format .joblib

joblib.dump(classifier, 'classifier.joblib')

print("Le modèle a été sauvegardé sous le nom 'model.joblib'.")

y_pred = train_evaluate.make_prediction(x_test, classifier)

# Evaluate model
print("les nombres de voisins plus proches  est ", args.n_neighbors)
train_evaluate.evaluate(y_test, y_pred, filename=OUTPUT_accuracy)
