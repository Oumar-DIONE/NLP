import requests

# URL de votre API
url = 'https://user-odione-90797-0.user.lab.sspcloud.fr/proxy/5000/predict'  # Remplacez par l'URL de votre API

# Envoyer une requête GET
response = requests.get(url)

# Vérifier si la requête a réussi (status code 200)
if response.status_code == 200:
    print("Réponse reçue avec succès:")
    print(response.json())  # Affiche la réponse sous forme JSON
else:
    print(f"Erreur {response.status_code}: {response.text}")
