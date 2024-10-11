
""" script documentation"""
import os

from botocore.exceptions import NoCredentialsError, ClientError
import pandas as pd
import boto3
import config


def download_from_s3(bucket_name, s3_key, local_file, minio_client):
    """Télécharge un fichier depuis un bucket S3.

    Paramètres:
    ----------
    bucket_name : str
        Le nom du bucket S3.
    s3_key : str
        La clé de l'objet à télécharger.
    local_file : str
        Le chemin local où le fichier sera enregistré.
    minio_client : Minio
        Instance de la bibliothèque Minio pour interagir avec S3.

    Renvoie:
    -------
    None
    """

    try:
        # Vérifiez si le fichier local existe, sinon créez-le
        local_dir = os.path.dirname(local_file)
        
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)  # Créez le répertoire parent si nécessaire
        
        # Téléchargez le fichier depuis le bucket S3
        minio_client.download_file(bucket_name, s3_key, local_file)
        print(f"Fichier {s3_key} téléchargé avec succès dans {local_file}.")

    except NoCredentialsError:
        print("Erreur : Aucune information d'identification valide n'a été trouvée.")
    except ClientError as e:
        print(f"Erreur lors du téléchargement du fichier : {e}")
    except OSError as e:
        print(f"Erreur lors de la création du fichier ou du répertoire : {e}")

# "/home/onyxia/work/NLP/configuration/config.yaml"


def load_data(config_path,data_path):
    """ what does this function"""
    config_dict = config.import_yaml_config(config_path)
    # Chemin de destination local
    path_in_s3 = config_dict.get("path_in_s3", "/.../")
    bucket_name = config_dict.get("bucket_name", "odione")
    endpoint_url = config_dict.get("endpoint_url", "0000")
    aws_access_key_id = config_dict.get("aws_access_key_id", "00")
    aws_secret_access_key = config_dict.get("aws_secret_access_key", "00")
    aws_session_token = config_dict.get("aws_session_token", "00")
    # Créez une session S3
    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token)

    print(" succesful connexion to s3 !")
    # Utilisation de la fonction
    download_from_s3(bucket_name, path_in_s3, data_path, s3)
    df = pd.read_csv(data_path)
    return df


def upload_to_s3(local_file, bucket_name, s3_key, miniocl):
    """
    Upload un fichier local vers un bucket S3.

    :param local_file: Chemin du fichier local à envoyer.
    :param bucket_name: Nom du bucket S3.
    :param s3_key: Chemin et nom de fichier dans le bucket S3.
    """
    
    # Créer le fichier local s'il n'existe pas
    if not os.path.exists(local_file):
        # Créer un fichier vide
        open(local_file, 'a').close()
        print(f"Le fichier {local_file} a été créé car il n'existait pas.")

    try:
        # Téléchargement du fichier vers S3
        miniocl.upload_file(local_file, bucket_name, s3_key)
        print(f"Fichier {local_file} envoyé avec succès vers {bucket_name}/{s3_key}.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {local_file} n'existe pas.")
    except NoCredentialsError:
        print("Erreur : Aucune information d'identification valide n'a été trouvée.")
    except ClientError as e:
        if e.response['Error']['Code'] == '403':
            print("Erreur 403 : Accès refusé. Vérifiez vos permissions S3.")
        elif e.response['Error']['Code'] == '404':
            print("Erreur 404 : Bucket introuvable.")
        else:
            print(f"Erreur lors de l'envoi du fichier : {e}")

# CONFIG_PATH="/home/onyxia/work/classification_K_Nearest_Neighbour/configuration/config.yaml")


def save_data_in_s3(config_path, local_file, path_in_s3):
    """ what are the parameters of this functions and what it  does"""
    config_dict = config.import_yaml_config(config_path)
    # Chemin de destination local
    bucket_name = config_dict.get("bucket_name", "odione")
    endpoint_url = config_dict.get("endpoint_url", "0000")
    aws_access_key_id = config_dict.get("aws_access_key_id", "00")
    aws_secret_access_key = config_dict.get("aws_secret_access_key", "00")
    aws_session_token = config_dict.get("aws_session_token", "00")
    # Créez une session S3
    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token)  # Ligne corrigée sans espace blanc

    print(" succesful connexion to s3 !")
    # Utilisation de la fonction

    upload_to_s3(local_file, bucket_name, path_in_s3, miniocl=s3)
    print("succeful data loading")
# l'utilise de la commande autopep8 --in-place --aggressive --aggressive import_data.py
# permet de supprimer les espaces blances automatiquements


def truncate_table(file_path):
    """ cette foncitonnera vider les tables qu'on a déja envoyé dans notre bcjet distant """
    # Ouvrir le fichier en mode écriture
    with open(file_path, 'w') as file:
        file.write('')  # Écrire une chaîne vide



