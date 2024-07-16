// Consumo de la API del backend
function enviarDatos(event) {
    event.preventDefault(); //Evitar que la página se recargue al enviar el formulario

    const data = {
        "Humidity": document.getElementById('humidity').value,
        "Wind Speed": document.getElementById('wind_speed').value,
        "Precipitation (%)": document.getElementById('precipitation').value,
        "Atmospheric Pressure": document.getElementById('pressure').value,
        "UV Index": document.getElementById('uv_index').value,
        "Visibility (km)": document.getElementById('visibility').value,
        "Cloud Cover": document.getElementById('cloud_cover').value,
        "Season": document.getElementById('season').value,
        "Location": document.getElementById('location').value,
        "Weather Type": document.getElementById('weather_type').value,
    }
    // data tiene los valores ingresados por el usuario

    const request = new Request('http://127.0.0.1:5000/predict', {
        method: 'POST',
        // encabezados
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        // cuerpo
    });

    fetch(request)
        // Promesas  ECMASCRIPT  
        .then(response => response.json()) // función anónima que convierte la respuesta en formato JSON

        .then(result => {
            document.getElementById('result').textContent = 'Temperatura: ' + result.Temperatura.toFixed(2);
        })

        .catch(error => {
            document.getElementById('result').textContent = 'Ocurrió un error' + error.message;
        })
}