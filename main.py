# Importing librairies
import sys
import os
import argparse
# Ajouter le chemin du dossier 'src/data' dans sys.path
sys.path.append(os.path.abspath("src/data"))
sys.path.append(os.path.abspath("src/models"))
sys.path.append(os.path.abspath("src/pipeline"))

import import_data
import build_features
import train_evaluate


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

# Load Data
dataset = import_data.load_data(CONFIG_PATH)

categorical = [var for var in dataset.columns if dataset[var].dtype == "O"]
numerical = [var for var in dataset.columns if dataset[var].dtype != "O"]


# Data preprocessing

# dataset["Email No."] = LabelEncoder().fit_transform(dataset["Email No."])

X, Y = build_features.encoder(dataset)

x_train, y_train, x_test, y_test = build_features.split_scale(X, Y)

# Build model

classifier = train_evaluate.knn_model(n_neighbors=args.n_neighbors, x=x_train, y=y_train)
# make prediction on test set

y_pred = train_evaluate.make_prediction(x_test, classifier)

# Evaluate model
print("les nombres de voisins plus proches  est ", args.n_neighbors)
train_evaluate.evaluate(y_test, y_pred)



