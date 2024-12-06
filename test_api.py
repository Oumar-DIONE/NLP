import requests

# URL de votre API
url = "https://user-odione-90797-0.user.lab.sspcloud.fr/proxy/5000/predict"

# Paramètres que vous souhaitez envoyer à l'API
params = {
    "sex": "female",
    "index": 1,
    "fare": 25.0,
    "embarked": "C"
}

# Effectuer la requête GET avec les paramètres
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Afficher la réponse JSON
    print(response.json())
else:
    print(f"Erreur {response.status_code}: {response.text}")
