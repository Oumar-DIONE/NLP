
import pandas as pd
import config
import boto3
CONFIG_PATH = "/home/onyxia/work/classification_K_Nearest_Neighbour/configuration/config.yaml"
config_dict = config.import_yaml_config(CONFIG_PATH)
DATA_PATH = config_dict.get("data_path", "emails.csv")
ENDPOINT_URL = config_dict.get("endpoint_url", "0000")
ACCESS_KEY_ID = config_dict.get("aws_access_key_id", "00")
SECRET_ACESS_KEY = config_dict.get("data_path", "00")
SESSION_TOKEN = config_dict.get("aws_session_token", "00")

s3 = boto3.client("s3",endpoint_url = ENDPOINT_URL,
                  aws_access_key_id = ACCESS_KEY_ID , 
                  aws_secret_access_key = SECRET_ACESS_KEY , 
                  aws_session_token = SESSION_TOKEN )

print(" succesful connexion to s3 !")
print("SESSION_TOKEN : ", SESSION_TOKEN)


def load_data(config_path=DATA_PATH):
    
    data_path = config_dict.get("data_path", "emails.csv")
    df = pd.read_csv(data_path)
    return df
    