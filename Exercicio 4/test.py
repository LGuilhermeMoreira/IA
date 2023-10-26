import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importando modelo de regressão linear
from sklearn import linear_model
# importando métricas para avaliação do modelo
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
# importando função para separar dados em treino e teste
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Prostate_Cancer.csv')

print(dataset.head())
