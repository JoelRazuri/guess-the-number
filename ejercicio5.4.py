"""
    Utilizando la función randrange del módulo random, escribir un programa que
    obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
    si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
    correcto.
"""


import random

print("ADIVINA EL NÚMERO")
print("")

numero_aleatorio = random.randrange(1,100)
flag = True

while flag:
    
    numero = int(input("Ingrese un número(entre 1 y 100): "))
    
    if numero == numero_aleatorio:
        flag = False
        print(f"Adivinaste el número: {numero_aleatorio}")
    else:
        if numero > numero_aleatorio:
            print("El número ingresado es mayor que el número aleatorio.")
        else:
            print("El número ingresado es menor que el número aleatorio.")




