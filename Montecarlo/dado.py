import random

def lanz_mon(num_intentos):
    cara = 0
    cruz = 0
    for _ in range(num_intentos):
        if(random.random()<0.5):
            cruz = cruz + 1
        else:
            cara = cara + 1
    
    probabilidad_caras = cara / num_intentos
    probabilidad_cruces = cruz / num_intentos

    return probabilidad_caras, probabilidad_cruces

intentos = 99999999
prob_caras, prob_cruces = lanz_mon(intentos)
print(f"La cantidad de veces que cayó cara fue: {prob_caras:.4f}")
print(f"La cantidad de veces que cayó cruz fue: {prob_cruces:.4f}")
    