import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

# Chemin vers le répertoire du projet
current_path = os.path.dirname(os.path.abspath(__file__))
# Récupérer le dossier parent immédiat
project_root = os.path.dirname(current_path)
OUTPUT_accuracy = os.path.join(current_path, os.getenv("OUTPUT_accuracy"))


score = pd.read_csv(current_path+"/"+os.getenv("OUTPUT_accuracy"))
print(score.values[0,1])