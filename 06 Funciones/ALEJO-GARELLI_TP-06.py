import math

# PARTE 1: DEFINICIÓN DE FUNCIONES

# 1. Función que solo imprime
def imprimir_hola_mundo():
    """Imprime 'Hola Mundo!' por pantalla."""
    print("Hola Mundo!")

# 2. Función que retorna un saludo
def saludar_usuario(nombre):
    """Recibe un nombre y devuelve un texto de saludo."""
    return f"Hola {nombre}!"

# 3. Función que imprime datos personales con formato
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Funciones para el círculo (Área y Perímetro)
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Conversión de segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar (Imprime directamente)
def tabla_multiplicar(numero):
    print(f"--- Tabla del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas (Retorna una tupla)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    # Evitamos división por cero con un condicional ternario
    div = a / b if b != 0 else "No definido"
    return (suma, resta, mult, div)

# 8. Cálculo de IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Conversión de temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3



# PARTE 2: PROGRAMA PRINCIPAL (PRUEBAS)

if __name__ == "__main__":
    print("\n>>> EJERCICIO 1: Hola Mundo")
    imprimir_hola_mundo()

    print("\n>>> EJERCICIO 2: Saludo personalizado")
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

    print("\n>>> EJERCICIO 3: Información Personal")
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    eda = input("Edad: ")
    res = input("Residencia: ")
    informacion_personal(nom, ape, eda, res)

    print("\n>>> EJERCICIO 4: Círculo")
    radio_usr = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio_usr)
    perimetro = calcular_perimetro_circulo(radio_usr)
    print(f"El área es: {area:.2f}")
    print(f"El perímetro es: {perimetro:.2f}")

    print("\n>>> EJERCICIO 5: Segundos a Horas")
    segs = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segs)
    print(f"Son {horas:.4f} horas.")

    print("\n>>> EJERCICIO 6: Tabla de Multiplicar")
    num_tabla = int(input("¿De qué número quieres la tabla?: "))
    tabla_multiplicar(num_tabla)

    print("\n>>> EJERCICIO 7: Operaciones Básicas")
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    # Guardamos la tupla que retorna la función
    resultados = operaciones_basicas(n1, n2)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

    print("\n>>> EJERCICIO 8: IMC")
    peso_usr = float(input("Ingresa tu peso (kg): "))
    altura_usr = float(input("Ingresa tu altura (m): "))
    imc = calcular_imc(peso_usr, altura_usr)
    print(f"Tu índice de masa corporal es: {imc:.2f}")

    print("\n>>> EJERCICIO 9: Temperatura")
    temp_c = float(input("Ingresa temperatura en °C: "))
    temp_f = celsius_a_fahrenheit(temp_c)
    print(f"Equivale a {temp_f} °F")

    print("\n>>> EJERCICIO 10: Promedio")
    print("Ingresa 3 notas:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    prom = calcular_promedio(nota1, nota2, nota3)
    print(f"El promedio es: {prom:.2f}")
    
    print("\n--- FIN DEL PROGRAMA ---")