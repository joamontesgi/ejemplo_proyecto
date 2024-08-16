from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Cargar el dataset 
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=42)

# Crear instancia de la técnica
knn = KNeighborsClassifier(n_neighbors=30)

# Entrenar el modelo
knn.fit(X_train, y_train)

# Predicción en el conjunto de datos de prueba
y_pred = knn.predict(X_test)

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

print(cm)

