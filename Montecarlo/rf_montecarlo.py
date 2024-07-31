import pandas
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Cargar el dataset
iris = load_iris()
X = iris.data
y = iris.target

# Número de simulaciones del método Montecarlo
n_iteraciones = 6
tam_prueba = 0.2
semilla = 42

# Almacenando los valores de la precisión
precisiones = []
# mejor_precision = 0
# mejor_modelo = None

for i in range(n_iteraciones):
    X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=tam_prueba, random_state=semilla+i)

    # Instanciar el modelo
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    
    # Evaluar la precisión del modelo
    precision = modelo.score(X_test, y_test)
    precisiones.append(precision)

# n = len(precisiones)
# for i in range(n):
#     print(precisiones[i])
# [90, 50, 80, 70, 99, 80]