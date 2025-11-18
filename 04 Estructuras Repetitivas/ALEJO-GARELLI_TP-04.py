import random  # Ejercicio 5

# Ejercicio 1

print("\n--- Ejercicio 1: Números del 0 al 100 ---")
contador = 0
while contador <= 100:
    print(contador)
    contador += 1



# Ejercicio 2

print("\n--- Ejercicio 2: Cantidad de dígitos ---")
numero = int(input("Ingrese un número entero: "))
temp_num = abs(numero)
cantidad_digitos = 0

if temp_num == 0:
    cantidad_digitos = 1
else:
    while temp_num > 0:
        temp_num = temp_num // 10  # Quita el último dígito
        cantidad_digitos += 1

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")



# Ejercicio 3

print("\n--- Ejercicio 3: Suma entre dos valores (excluyentes) ---")
val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))

# Determinamos cuál es el menor y cuál el mayor
menor = min(val1, val2)
mayor = max(val1, val2)

suma_total = 0
actual = menor + 1

while actual < mayor:
    suma_total += actual
    actual += 1

print(f"La suma de los enteros entre {menor} y {mayor} es: {suma_total}")



# Ejercicio 4

print("\n--- Ejercicio 4: Suma secuencial (corte con 0) ---")
acumulador = 0
continuar = True

print("Ingrese números para sumar. Ingrese 0 para finalizar.")

while continuar:
    numero = int(input("Número: "))
    
    if numero == 0:
        continuar = False
    else:
        acumulador += numero

print(f"Total acumulado: {acumulador}")



# Ejercicio 5

print("\n--- Ejercicio 5: Adivinar el número (0-9) ---")
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("Adivine el número secreto entre 0 y 9.")

while not adivinado:
    intento_usuario = int(input("Su intento: "))
    intentos += 1
    
    if intento_usuario == numero_secreto:
        adivinado = True
    else:
        print("Incorrecto, intente de nuevo.")

print(f"¡Correcto! El número era {numero_secreto}. Cantidad de intentos: {intentos}")



# Ejercicio 6

print("\n--- Ejercicio 6: Pares del 0 al 100 (decreciente) ---")
contador = 100

while contador >= 0:
    if contador % 2 == 0:  # Es par
        print(contador, end=" ") 
    contador -= 1
print() # Salto de línea



# Ejercicio 7

print("\n--- Ejercicio 7: Suma de 0 hasta N ---")
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
actual = 0

if limite < 0:
    print("El número debe ser positivo.")
else:
    while actual <= limite:
        suma += actual
        actual += 1
    print(f"La suma de 0 hasta {limite} es: {suma}")



# Ejercicio 8

print("\n--- Ejercicio 8: Estadísticas de números ---")
cien = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Se solicitarán {cien} números.")

for i in range(cien):
    num = int(input(f"Ingrese número {i+1}: "))
    
    # Paridad
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Signo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")



# Ejercicio 9

print("\n--- Ejercicio 9: Calcular media (promedio) ---")
TOTAL_NUMEROS = 100 

suma_acumulada = 0

print(f"Se solicitarán {TOTAL_NUMEROS} números.")

for i in range(TOTAL_NUMEROS):
    valor = int(input(f"Ingrese valor {i+1}: "))
    suma_acumulada += valor

media = suma_acumulada / TOTAL_NUMEROS
print(f"La media de los valores ingresados es: {media}")



# Ejercicio 10

print("\n--- Ejercicio 10: Invertir número ---")
numero_original = int(input("Ingrese un número para invertir: "))
numero_aux = abs(numero_original)
numero_invertido = 0

while numero_aux > 0:
    digito = numero_aux % 10              # Último dígito
    numero_invertido = (numero_invertido * 10) + digito 
    numero_aux = numero_aux // 10         # Eliminar el último dígito del original

# Si el original era negativo, ajustamos el signo
if numero_original < 0:
    numero_invertido = numero_invertido * -1

print(f"Número invertido: {numero_invertido}")

print("\n--- Fin de los ejercicios ---")