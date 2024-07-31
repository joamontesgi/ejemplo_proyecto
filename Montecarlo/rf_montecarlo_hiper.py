from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd 
import numpy as np 

n_estimadores = [50, 100, 200, 500, 1000] 
profundidad = [5, 10, 20, 30, 40]

datos = load_iris()
X = datos.data
y = datos.target

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

def monte_carlo_simulacion(n_intentos, n_estimadores, profundidad):
    resultados = []
    
    for i in range(n_intentos):
        
        #Seleccionando aleatoriamente los hiperparámetros
        estimador = np.random.choice(n_estimadores)
        prof = np.random.choice(profundidad)
        
        # Crear el modelo
        modelo = RandomForestClassifier(n_estimators=estimador, max_depth=prof, random_state=42)
        modelo.fit(X_entrenamiento, y_entrenamiento)
        
        y_pred = modelo.predict(X_prueba)
        precision = accuracy_score(y_prueba, y_pred)
        
        resultados.append(
            {
                'estimador': estimador,
                'profundidad': prof,
                'precision':precision
            }
        )
    
    return pd.DataFrame(resultados)

n_intentos = 10
resultados = monte_carlo_simulacion(n_intentos, n_estimadores, profundidad)
print(resultados)


    
    
    

