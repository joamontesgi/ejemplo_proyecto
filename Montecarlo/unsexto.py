import random

def lanz_dado(intentos):
    
    # Lista para guardar las ocurrencias de cada lado
    ocurr_lados = [0] * 6
    
    # Realizar simulación
    for _ in range(intentos):
        dado = random.randint(1, 6) # Simulando el lanzamiento del dado
        ocurr_lados[dado - 1] +=1

    # Calcular las probabilidad
    probabilidades = [0] * 6
    
    for i in range(6):
        probabilidades[i] = ocurr_lados[i] / intentos
    
    return probabilidades

# Ejecución simulación
num_intentos = 99999
probabilidades = lanz_dado(num_intentos)

# Mostrar las probabilidad en cada posición de la lista
for i in range(6):
    print(f"Probabilidad de {i+1}: {probabilidades[i]:.4f}")

    