from fastapi import FastAPI, HTTPException
from joblib import load
import pandas as pd

# Charger le modèle pré-entraîné
model = load('classifier.joblib')
X = pd.read_csv("X.csv").values  # Charger les données directement sous forme de tableau

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
    sex: str = "female",
    index: int = 0,
    fare: float = 16.5,
    embarked: str = "S"
) -> dict:
    """
    Prédit la survie ou la mort d'une personne en fonction des données fournies.
    """
    # Validation de l'index
    if index < 0 or index >= len(X):
        raise HTTPException(status_code=400, detail="Index out of range")

    # Récupérer la ligne correspondante et effectuer une prédiction
    ligne_i = X[index].reshape(1, -1)
    prediction = "Survived 🎉" if int(model.predict(ligne_i)) == 1 else "Dead ⚰️"

    # Retourner le résultat sous forme d'objet JSON
    return {
        "index": index,
        "prediction": prediction,
        "message": f"La prédiction a été effectuée pour la donnée à la position {index}.",
    }
