# Ejercicio 1...

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad.")


# Ejercicio 2...

nota = int(input("Ingrese la nota obtenida: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3...

num = float(input("Ingrese un numero par: "))
if (num % 2) == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par.")


# Ejercicio 4...

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
    print("Eres un niño.")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un adulto joven.")
else:
    print("Eres un adulto mayor.")


# Ejercicio 5...

contra = input("Ingrese su contraseña: ")
largo = len(contra)

if largo >= 8 and largo <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# Ejercicio 6...

import random
from statistics import mean, median, mode


numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
print("Lista generada:", numeros_aleatorios)

# Calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios) 
except:
    moda = "No definida (varias modas)"

print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar el sesgo
if isinstance(moda, (int, float)):   
    if media > mediana and mediana > moda:
        print("Distribución con SESGO POSITIVO (a la derecha).")
    elif media < mediana and mediana < moda:
        print("Distribución con SESGO NEGATIVO (a la izquierda).")
    elif media == mediana == moda:
        print("Distribución SIN SESGO.")
    else:
        print("Distribución sin sesgo claro (valores intermedios).")
else:
    print("No se pudo determinar el sesgo porque hay varias modas.")


# Ejercicio 7...

frase = input("Ingrese una frase o palabra: ")
ult_caracter = frase[-1]
vocal = 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'

if ult_caracter in vocal:
    print(f"{frase}!")
else:
    print(frase)


# Ejercicio 8...

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese la opcion deseada (1, 2 o 3): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion incorrecta.")


# Ejercicio 9...

print("Clasificación de terremoto.")
terremoto = float(input("Ingrese la magnitud del terremoto: "))

#Condiciones
if terremoto > 0:
    if terremoto < 3:
        print("Muy leve (imperceptible).")
    elif terremoto >= 3 and terremoto < 4:
        print("Leve (ligeramente perceptible).")
    elif terremoto >= 4 and terremoto < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños).")
    elif terremoto >= 5 and terremoto < 6:
        print("Fuerte (puede causar daños en estructuras débiles).")
    elif terremoto >= 6 and terremoto < 7:
        print("Muy Fuerte (puede causar daños significativos).")
    elif terremoto >= 7:
        print("Extremo (puede causar graves daños a gran escala).")
#Solo permitir ingresar numeros mayores a 0
else:
    print("No hubo terremoto o fue menor que una escala imperceptible.")


# Ejercicio 10...

print("Ingrese los siguientes datos...")
hemis = input("Hemisferio que te encuentras (N/S): ").upper()
mes = int(input("Mes actual (1-12): "))
dia = int(input("Dia actual: "))

# Desde 21 de diciembre hasta 20 de marzo
if ((dia >= 21 and dia <= 31) and mes == 12) or ((dia <= 20 and dia >= 1) and mes == 3) or ((dia <= 31 and dia >= 1) and mes == 1 or (dia <= 28 and dia >= 1 ) and mes == 2):
    if hemis == 'N':
        print("Te encuentras en INVIERNO.")
    elif hemis == 'S':
        print("Te encuentras en VERANO.")
    else:
        print("Error. Ingrese S/N")

# Desde 21 de marzo hasta 20 de junio
elif ((dia >= 21 and dia <= 31) and mes == 3) or ((dia <= 20 and dia >= 1) and mes == 6) or ((dia <= 30 and dia >= 1) and mes == 4 or (dia <= 31 and dia >= 1) and mes == 5):
    if hemis == 'N':
        print("Te encuentras en PRIMAVERA.")
    elif hemis == 'S':
        print("Te encuentras en OTOÑO.")
    else:
        print("Error. Ingrese S/N")

# Desde 21 de junio hasta 20 de septiembre
elif ((dia >= 21 and dia <= 30) and mes == 6) or ((dia <= 20 and dia >= 1) and mes == 9) or ((dia <= 31 and dia >= 1) and mes == 7 or (dia <= 31 and dia >= 1) and mes == 8):
    if hemis == 'N':
        print("Te encuentras en VERANO.")
    elif hemis == 'S':
        print("Te encuentras en INVIERNO.")
    else:
        print("Error. Ingrese S/N")

# Desde 21 de septiembre hasta 20 de diciembre
elif ((dia >= 21 and dia <= 30) and mes == 9) or ((dia <= 20 and dia >= 1) and mes == 12) or ((dia <= 31 and dia >= 1) and mes == 10) or ((dia <= 30 and dia >= 1) and mes == 11):
    if hemis == 'N':
        print("Te encuentras en OTOÑO.")
    elif hemis == 'S':
        print("Te encuentras en PRIMAVERA.")
    else:
        print("Error. Ingrese S/N")

else:
    print("Datos incorrectos, intente nuevamente.")