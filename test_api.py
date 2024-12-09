import requests

url = "http://127.0.0.1:8000/predict?military=1&index=10&enhancements=0&connevey=1"

# Effectuer la requête
response = requests.get(url)

# Vérifier si la réponse a un statut HTTP valide (200 OK)
if response.status_code == 200:
    try:
        # Essayer de convertir la réponse en JSON
        data = response.json()
        print(data)
    except ValueError:
        # En cas d'erreur lors du parsing JSON
        print("La réponse n'est pas au format JSON.")
else:
    print(f"Erreur HTTP {response.status_code}: {response.text}")
