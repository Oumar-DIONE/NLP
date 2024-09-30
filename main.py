import numpy as np
import random as rd
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Ignorer tous les avertissements
warnings.filterwarnings("ignore")
# Fixer les graines des mes différenets générateurs de nombres aleatoires afin de rendre mes resultats reproductibles
np.random.seed(0)
rd.seed(0)

print("TF Version: ", tf.__version__)
print("Hub version: ", hub.__version__)


# filesystem
input_dir="/home/onyxia/work/NLP/"
output_dir="/home/onyxia/work/NLP/Outputs/"
codes_dir="/home/onyxia/work/NLP//Codes/"
file1="firstname_with_sex.csv"
file2="transcriptions_with_sex.csv"
# preprocessing
scale=0.2
# Python interpretatot(which python)
path_python="/opt/conda/bin/python"

#model
df1=pd.read_csv(input_dir+file1,sep=";")
print("Shape :" ,df1.shape )
