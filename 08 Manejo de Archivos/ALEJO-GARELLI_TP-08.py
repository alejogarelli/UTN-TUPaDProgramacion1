import os

NOMBRE_ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    # ---EJERCICIO 1---

    datos = [
        "Lapicera,120.5,30",
        "Cuaderno,500.0,10",
        "Goma,50.0,50"
    ]
    
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for linea in datos:
            archivo.write(linea + "\n")
    print("Ejercicio 1: Archivo creado.")

def cargar_productos():

    productos = []
    
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "r") as archivo:
            for linea in archivo:
                linea = linea.strip() # ---EJERCICIO 2---
                if len(linea) > 0:
                    datos = linea.split(",") # ---EJERCICIO 2---
                    
                    # ---EJERCICIO 4---
                    diccionario_producto = {
                        "nombre": datos[0],
                        "precio": float(datos[1]),
                        "cantidad": int(datos[2])
                    }
                    productos.append(diccionario_producto)
    
    return productos

def mostrar_productos(productos):
    
    # ---EJERCICIO 2---
    print("\n--- Listado de Productos (Ejercicio 2) ---")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto_teclado():
    
    # ---EJERCICIO 3---
    print("\n--- Agregar Producto (Ejercicio 3) ---")
    nombre = input("Ingrese nombre: ")
    precio = input("Ingrese precio: ")
    cantidad = input("Ingrese cantidad: ")
    
    with open(NOMBRE_ARCHIVO, "a") as archivo:
        archivo.write(f"\n{nombre},{precio},{cantidad}")
    print("Producto agregado correctamente.")

def buscar_producto(productos):
    
    # ---EJERCICIO 5---
    print("\n--- Buscar Producto (Ejercicio 5) ---")
    nombre_buscado = input("Ingrese nombre a buscar: ").lower()
    
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscado:
            print(f"Encontrado -> Nombre: {p['nombre']}, Precio: ${p['precio']}, Cantidad: {p['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print("Error: Producto no encontrado.")

def guardar_todo(productos):
    
    # ---EJERCICIO 6---
    print("\n--- Guardar Cambios (Ejercicio 6) ---")
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)
    print("Archivo sobrescrito con exito.")

def main():
    # Ejecución de los ejercicios 1 al 6
    
    # 1. Crear archivo
    crear_archivo_inicial()
    
    # 2. y 4. Leer archivo y cargar lista
    productos = cargar_productos()
    mostrar_productos(productos)
    
    # 3. Agregar producto nuevo
    agregar_producto_teclado()
    
    # Actualizamos la lista
    productos = cargar_productos()
    
    # 5. Buscar producto
    buscar_producto(productos)
    
    # 6. Guardar todo (sobrescritura)
    guardar_todo(productos)

if __name__ == "__main__":
    main()