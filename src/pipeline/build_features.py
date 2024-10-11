""" packages docstrings """
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def encoder(data_set):
    """ encodage du variables binaires en 0-1 """
    # use LabelEncoder to replace purchased (dependent variable) with 0 and 1
    data_set["Email No."] = LabelEncoder().fit_transform(data_set["Email No."])
    y = data_set["Prediction"]
    x = data_set.drop(["Prediction"], axis=1)
    return x, y


def split_scale(xset, yset, test_size=0.3):
    """ split and scale the data """
    # Splitting the dataset  into  training  and test set
    x, xt, y, yt = train_test_split(xset, yset, test_size=test_size, random_state=0)
    # func returns train and test data. It takes dataset and
    # then split size test_size =0.3 means 30% data is for test and  
    # rest for training and random_state
    scaler = StandardScaler()
    x = scaler.fit_transform(x)  # apply on whole x data
    xt = scaler.transform(xt)
    return x, y, xt, yt
