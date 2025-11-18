import random # Ejercicio 3 y 10

# Ejercicio 1

print("\n--- Ejercicio 1: Notas de Estudiantes ---")
notas = [7, 8, 5, 9, 10, 4, 6, 8, 9, 7]

print("Lista de notas:", notas)

# Promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)

# Máximo y mínimo
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")



# Ejercicio 2

print("\n--- Ejercicio 2: Gestión de Productos ---")
productos = []

print("Por favor, cargue 5 productos:")
for i in range(5):
    prod = input(f"Ingrese producto {i+1}: ").strip().capitalize()
    productos.append(prod)

productos_ordenados = sorted(productos)
print("\nLista ordenada alfabéticamente:", productos_ordenados)

# Eliminar producto
eliminar = input("\n¿Qué producto desea eliminar? (Ingrese el nombre): ").strip().capitalize()

if eliminar in productos:
    productos.remove(eliminar)
    print(f"Producto '{eliminar}' eliminado.")
    print("Lista actualizada:", productos)
else:
    print("El producto no se encuentra en la lista.")



# Ejercicio 3

print("\n--- Ejercicio 3: Pares e Impares Aleatorios ---")
numeros_azar = []
pares = []
impares = []

for _ in range(15):
    numeros_azar.append(random.randint(1, 100))

# Clasificamos
for num in numeros_azar:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista generada:", numeros_azar)
print(f"Pares ({len(pares)}):", pares)
print(f"Impares ({len(impares)}):", impares)



# Ejercicio 4

print("\n--- Ejercicio 4: Eliminar Duplicados ---")
lista_original = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_repetir = []

for numero in lista_original:
    if numero not in lista_sin_repetir:
        lista_sin_repetir.append(numero)

print("Original:", lista_original)
print("Sin repetidos:", lista_sin_repetir)



# Ejercicio 5

print("\n--- Ejercicio 5: Asistencia ---")
estudiantes = ["Alejo", "Luis", "Francisco", "Julia", "Sofía", "Javier", "Lucía", "Joaquin"]
print("Estudiantes presentes:", estudiantes)

accion = input("\n¿Desea (A)gregar o (E)liminar un estudiante? ").upper()

if accion == 'A':
    nuevo = input("Nombre del nuevo estudiante: ").strip().capitalize()
    estudiantes.append(nuevo)
    print("Estudiante agregado.")
elif accion == 'E':
    nombre_borrar = input("Nombre del estudiante a eliminar: ").strip().capitalize()
    if nombre_borrar in estudiantes:
        estudiantes.remove(nombre_borrar)
        print("Estudiante eliminado.")
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Opción no válida.")

print("Lista final:", estudiantes)



# Ejercicio 6

print("\n--- Ejercicio 6: Rotación de Lista ---")
numeros = [10, 20, 30, 40, 50, 60, 70]
print("Antes de rotar:", numeros)


ultimo_elemento = numeros.pop() 
numeros.insert(0, ultimo_elemento)

print("Después de rotar:", numeros)



# Ejercicio 7

print("\n--- Ejercicio 7: Temperaturas Semanales (Matriz 7x2) ---")

semana = [
    [12, 25], # Día 1
    [15, 28], # Día 2
    [10, 22], # Día 3
    [18, 30], # Día 4
    [14, 26], # Día 5
    [16, 29], # Día 6
    [13, 24]  # Día 7
]

suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(len(semana)):
    minima = semana[i][0]
    maxima = semana[i][1]
    
    suma_minimas += minima
    suma_maximas += maxima
    
    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

prom_min = suma_minimas / 7
prom_max = suma_maximas / 7

print(f"Promedio Mínimas: {prom_min:.2f}")
print(f"Promedio Máximas: {prom_max:.2f}")
print(f"Mayor amplitud térmica ({mayor_amplitud} grados) registrada el Día {dia_mayor_amplitud}.")



# Ejercicio 8

print("\n--- Ejercicio 8: Matriz de Notas (5x3) ---")
# Filas: Estudiantes, Columnas: Materias
notas_matriz = [
    [7, 8, 9], # Estudiante 1
    [6, 6, 7], # Estudiante 2
    [9, 9, 10],# Estudiante 3
    [4, 5, 5], # Estudiante 4
    [8, 7, 8]  # Estudiante 5
]

# 1. Promedio de cada estudiante
print("Promedios por Estudiante:")
for i in range(len(notas_matriz)):
    suma_est = sum(notas_matriz[i])
    prom_est = suma_est / 3
    print(f" - Estudiante {i+1}: {prom_est:.2f}")

# 2. Promedio de cada materia
print("\nPromedios por Materia:")
for col in range(3): 
    suma_materia = 0
    for fila in range(5):
        suma_materia += notas_matriz[fila][col]
    
    prom_materia = suma_materia / 5
    print(f" - Materia {col+1}: {prom_materia:.2f}")



# Ejercicio 9

print("\n--- Ejercicio 9: Ta-Te-Ti Simplificado ---")

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugadas = 0
turno = "X"

print("Instrucciones: Ingrese fila (0-2) y columna (0-2).")

# Permitimos 9 jugadas máximo (tablero lleno)
while jugadas < 9:
    for fila in tablero:
        print(" ".join(fila))
    
    print(f"\nTurno del jugador {turno}")
    try:
        f = int(input("Fila (0, 1, 2): "))
        c = int(input("Columna (0, 1, 2): "))
        
        if 0 <= f <= 2 and 0 <= c <= 2:
            if tablero[f][c] == "-":
                tablero[f][c] = turno
                jugadas += 1
                # Cambiar turno
                if turno == "X":
                    turno = "O"
                else:
                    turno = "X"
            else:
                print("¡Casilla ocupada! Intente de nuevo.")
        else:
            print("Coordenadas fuera de rango.")
            
    except ValueError:
        print("Por favor ingrese números enteros.")

print("\nJuego terminado (tablero lleno o interrumpido).")
for fila in tablero:
    print(" ".join(fila))



# Ejercicio 10

print("\n--- Ejercicio 10: Matriz de Ventas (4x7) ---")

ventas = []
for p in range(4):
    fila_producto = []
    for d in range(7):
        fila_producto.append(random.randint(10, 50))
    ventas.append(fila_producto)

# Matriz generada
print("Matriz de ventas generada:")
for fila in ventas:
    print(fila)

# 1. Total vendido por producto
print("\nTotal por Producto:")
max_ventas_prod = -1
producto_estrella = -1

for i in range(4):
    total_prod = sum(ventas[i])
    print(f" - Producto {i+1}: {total_prod} unidades")
    
    # Mas vendido
    if total_prod > max_ventas_prod:
        max_ventas_prod = total_prod
        producto_estrella = i + 1

# 2. Día con mayores ventas totales
max_ventas_dia = -1
mejor_dia = -1

for col in range(7):
    suma_dia = 0
    for fila in range(4):
        suma_dia += ventas[fila][col]
    
    if suma_dia > max_ventas_dia:
        max_ventas_dia = suma_dia
        mejor_dia = col + 1

print(f"\nEl día con mayores ventas fue el Día {mejor_dia} (Total: {max_ventas_dia})")
print(f"El producto más vendido en la semana fue el Producto {producto_estrella}")

print("\n--- Fin del Trabajo Práctico ---")