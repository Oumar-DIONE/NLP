
import pandas as pd
import config


def load_data(config_path):
    config_dict = config.import_yaml_config(config_path)
    data_path = config_dict.get("data_path", "emails.csv")
    df = pd.read_csv(data_path)
    return df
    