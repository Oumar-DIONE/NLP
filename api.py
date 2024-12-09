from fastapi import FastAPI, HTTPException
from joblib import load
import pandas as pd

# Charger le modèle pré-entraîné
model = load('classifier.joblib')
X = pd.read_csv("X.csv")  # Charger les données directement sous forme de tableau

# Initialiser l'application FastAPI
app = FastAPI(
    title="Prédiction de survie sur le Titanic",
    description="Application de prédiction de survie sur le Titanic 🚢 <br>Une version par API pour faciliter la réutilisation du modèle 🚀"
)


@app.get("/", tags=["Welcome"])
def show_welcome_page():
    """
    Affiche la page d'accueil avec le nom et la version du modèle.
    """
    return {
        "Message": "API de prédiction de survie sur le Titanic",
        "Model_name": "Titanic ML",
        "Model_version": "0.1",
    }


@app.get("/owner", tags=["Owner"])
def owner():
    """
    Affiche les informations sur le propriétaire de l'API.
    """
    return {
        "Name": "DIONE",
        "First name": "Oumar",
        "Birthdays": "21 juillet 1995",
    }


@app.get("/predict", tags=["Predict"])
async def predict(
    military: int = 0,
    index: int = 0,
    enhancements: int = 0,
    connevey: int = 0
) -> dict:
    """
    Prédit la survie ou la mort d'une personne en fonction des données fournies.
    """

    # Validation de l'index
    if index < 0 or index >= len(X):
        raise HTTPException(status_code=400, detail="Index out of range")

    # Créer un dataframe avec les nouvelles données
    df = pd.DataFrame(
        {
            "military": [military],
            "enhancements": [enhancements],
            "connevey": [connevey],
            "index": [index],
        }
    )

    # Copier la ligne correspondante de X et la modifier
    df_test = X.iloc[index].copy()
    df_test["military"] = int(df["military"].iloc[0])
    df_test["enhancements"] = int(df["enhancements"].iloc[0])
    df_test["connevey"] = int(df["connevey"].iloc[0])

    # Récupérer les données pour la prédiction
    ligne_i = df_test.values.reshape(1, -1)
    prediction = "Survived 🎉" if (model.predict(ligne_i) == 1)[0] else "Dead ⚰️"

    # Retourner le résultat avec les types natifs
    return {
        "index": int(index),
        "prediction": prediction,
        "message": f"La prédiction a été effectuée pour la donnée à la position {index}.",
    }

#Exemple d'URL pour tester directement (sans Swagger UI)
#Vous pouvez aussi envoyer des requêtes directement dans votre navigateur en construisant l'URL. Par exemple :

#perl
#Copier le code
#http://127.0.0.1:8000/predict?military=1&index=10&enhancements=0&connevey=1
#https://user-odione-90797-0.user.lab.sspcloud.fr/proxy/5000/predict?military=1&index=10&enhancements=0&connevey=1