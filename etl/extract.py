from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import schedule  # Tarea programada
import time

def extraer():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Eivta que se abra una ventana del navegador
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.worldometers.info/es/poblacion-mundial/')
    elements = driver.find_elements(By.ID, 'maincounter-wrap')
    data = {}
    for element in elements:
        key = element.find_element(By.TAG_NAME, 'h1').text
        key = key.replace('ó', 'o')
        value = element.find_element(By.TAG_NAME, 'span').text
        data[key] = value
    driver.quit()
    
    with open('datos.txt', 'a') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    return "OK"

schedule.every(10).seconds.do(extraer)

while True:
    schedule.run_pending()
