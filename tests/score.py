import os
import pandas as pd
from dotenv import load_dotenv

# Chemin vers le répertoire du projet
current_path = os.path.dirname(os.path.abspath(__file__))
# Récupérer le dossier parent immédiat
project_root = os.path.dirname(current_path)
load_dotenv(dotenv_path=project_root+"/"+".env")
OUTPUT_accuracy = os.path.join(project_root, os.getenv("OUTPUT_accuracy"))
score = pd.read_csv(OUTPUT_accuracy)
accuracy=score.values[0,1]
if( accuracy>0.7):
    print("le modèle semble  pas si mal")
else:
    print("le modèle n'est trés fiable")

print(accuracy)

