import PyPDF2
import json

def extraer_texto(archivo):
    with open(archivo, 'rb') as file:
        texto = ""
        lector = PyPDF2.PdfReader(file)
        n = len(lector.pages)
        for num_pag in range(n):
            # Obtenemos la página actual usando el índice
            pagina = lector.pages[num_pag]
            texto += pagina.extract_text()
    return texto

ruta_archivo = 'parcial.pdf'
texto_pdf = extraer_texto(ruta_archivo)

datos = {
    'contenido_del_parcial': texto_pdf
}

with open('parcial_json_pdf.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(datos, archivo_json, indent=4)
print("Se han guardado los datos con éxito")