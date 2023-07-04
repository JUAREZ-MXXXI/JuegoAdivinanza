import random
import threading

print("Adivina un número del 1 al 100")

def adivina_numero():
    numero = random.randint(1, 100)
    intentos = 0
    adivinado = False

    def tiempo_agotado():
        nonlocal adivinado
        if not adivinado:
            print("¡Tiempo agotado! Perdiste.")
            adivinado = True

    while True:
        t = threading.Timer(20.0, tiempo_agotado)
        t.start()

        while not adivinado:
            intento = int(input("Adivina el número: "))
            intentos += 1

            if intento == numero:
                print(f"¡Adivinaste en {intentos} intentos!")
                adivinado = True
            elif intento < numero:
                print("El número es más grande. Intenta de nuevo.")
            else:
                print("El número es más pequeño. Intenta de nuevo.")

        t.cancel()

        respuesta = input("¿Deseas volver a jugar? (s/n): ")
        if respuesta.lower() != "s":
            break
        
        numero = random.randint(1, 100)
        intentos = 0
        adivinado = False

adivina_numero()
