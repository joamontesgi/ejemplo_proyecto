# API FLASK
from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS #(Cross-origin resource sharing)

app = Flask(__name__)
CORS(app)

model = joblib.load('regresion_lineal.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() #Obtener los datos del request
        input_data = pd.DataFrame([data]) #Convertir los datos en dataframe
        input_data = pd.get_dummies(input_data) #Codificar las variables categóricas
        
        input_data = input_data.reindex(columns=model_columns, fill_value=0)
        #Reordenar las columnas del df para que sean iguales a las del modelo.
        #Cuando falte una columna, los valores faltantes serán 0
        
        #Encontrar la predicción
        prediction = model.predict(input_data)
        
        #Retornar la predicción
        return jsonify({'Temperatura': prediction[0]})
    except Exception as e:
        return jsonify({'Error': str(e)})




if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
    