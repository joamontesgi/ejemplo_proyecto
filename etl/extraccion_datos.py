from bs4 import BeautifulSoup
import json 
import requests

sitio_web = 'https://www.elespectador.com/'

peticion = requests.get(sitio_web)

# Crear un objeto para analizar el código HTML
soup = BeautifulSoup(peticion.content, 'html.parser')

# Buscar en el sitio web los enlaces
enlaces = soup.find_all('a')

data = []

for enlace in enlaces:
    data.append({
        'Enlace': enlace.get('href'),
        'Texto': enlace.text
    })
    
with open('hipervinculos.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=4)

print("Se guardaron los datos con éxito")

# GET: OBTENER DATOS
# POST: ENVIAR DATOS
# DELETE: ELIMINAR DATOS
# PUT: ACTUALIZAR DATOS  -> NOMBRE, APELLIDO, TEL, DOC
# PATCH: ACTUALIZAR DATOS -> APELLIDO
