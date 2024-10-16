""" package docstrings """
# /home/headless/work/NLP
# Importing librairies
# pylint: disable=wrong-import-position

import sys
import os
import argparse
from dotenv import load_dotenv


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
load_dotenv()

# Récupérer le chemin des données depuis la variable d'environnement
DATA_PATH = os.getenv('DATA_PATH')
CONFIG_PATH = os.getenv('CONFIG_PATH')
Output_X_PATH = os.getenv('Output_X_PATH')
Output_Y_PATH = os.getenv('Output_Y_PATH')


# Load Data
dataset = import_data.load_data(CONFIG_PATH, DATA_PATH)
# vider le contenu de la table emails qui est locument inutiles
# car on a les données dans datasets (temporairement et c'est suffisants).
import_data.truncate_table(DATA_PATH)

categorical = [var for var in dataset.columns if dataset[var].dtype == "O"]
numerical = [var for var in dataset.columns if dataset[var].dtype != "O"]


# Data preprocessing

# dataset["Email No."] = LabelEncoder().fit_transform(dataset["Email No."])

X, Y = build_features.encoder(dataset)
# Sauvegarder les données transfomées par l'étape  de préprocessing 
X.to_csv(Output_X_PATH, index=False, encoding='utf-8')
Y.to_csv(Output_Y_PATH, index=False, encoding='utf-8')
x_train, y_train, x_test, y_test = build_features.split_scale(X, Y)
# Vider les deux tables qui viennent d'être envoyées dans le bucket distant
import_data.truncate_table(Output_X_PATH)
import_data.truncate_table(Output_Y_PATH)


print("Le fichier CSV a été sauvegardé avec succès.")
# Envoyer les données transfomées dans mon buckets S3 puis vider localement ces dataframes 
BUCKET_NAME = os.getenv('BUCKET_NAME')
import_data.save_data_in_s3(CONFIG_PATH, Output_X_PATH, path_in_s3="EMAIL_DATA/X.csv")
import_data.save_data_in_s3(CONFIG_PATH, Output_Y_PATH, path_in_s3="EMAIL_DATA/Y.csv")# Build model

classifier = train_evaluate.knn_model(
    n_neighbors=args.n_neighbors, x=x_train, y=y_train)
# make prediction on test set

y_pred = train_evaluate.make_prediction(x_test, classifier)

# Evaluate model
print("les nombres de voisins plus proches  est ", args.n_neighbors)
train_evaluate.evaluate(y_test, y_pred)
