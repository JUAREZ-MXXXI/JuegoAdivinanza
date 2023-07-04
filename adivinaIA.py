import random

print("Adivina un número del 1 al 100")

def adivina_numero():
    numero = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    # Implementación de la IA utilizando búsqueda binaria
    limite_inferior = 1
    limite_superior = 100
    prediccion = (limite_inferior + limite_superior) // 2
    
    while not adivinado:
        intentos += 1
        
        if prediccion == numero:
            print(f"¡La IA adivinó el número {numero} en {intentos} intentos!")
            adivinado = True
        elif prediccion < numero:
            print(f"La IA predijo {prediccion}. El número es más grande.")
            limite_inferior = prediccion + 1
            prediccion = (limite_inferior + limite_superior) // 2
        else:
            print(f"La IA predijo {prediccion}. El número es más pequeño.")
            limite_superior = prediccion - 1
            prediccion = (limite_inferior + limite_superior) // 2

adivina_numero()