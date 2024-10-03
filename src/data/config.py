import os
import yaml

#filename_="/home/onyxia/work/classification_K_Nearest_Neighbour/configuration/config.yaml"
def import_yaml_config(filename_="/home/headless/work/NLP/config.yaml"):
    config = {}
    if os.path.exists(filename_):
        # lecture du fichier
        with open(filename_, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    return config
   