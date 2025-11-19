def main():
    # ---EJERCICIO 1---
    print("\n--- EJERCICIO 1 ---")
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print(f"Diccionario inicial completado: {precios_frutas}")

   
    # ---EJERCICIO 2---
    print("\n--- EJERCICIO 2 ---")
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    
    print(f"Diccionario con precios actualizados: {precios_frutas}")


    # ---EJERCICIO 3---
    print("\n--- EJERCICIO 3 ---")
    lista_frutas = list(precios_frutas.keys())
    print(f"Lista solo de frutas: {lista_frutas}")


    # ---EJERCICIO 4---
    print("\n--- EJERCICIO 4 ---")
    contactos = {}
    
    # Cargar 5 contactos
    print("Por favor, cargue 5 contactos:")
    for i in range(5):
        nombre = input(f"Nombre del contacto {i+1}: ").capitalize()
        numero = input(f"Número de {nombre}: ")
        contactos[nombre] = numero
    
    # Consultar
    busqueda = input("Ingrese el nombre a buscar: ").capitalize()
    if busqueda in contactos:
        print(f"El número de {busqueda} es: {contactos[busqueda]}")
    else:
        print("El contacto no existe.")


    # ---EJERCICIO 5---
    print("\n--- EJERCICIO 5 ---")
    frase = input("Ingresá una frase: ").lower()
    palabras = frase.split()
    unicas = set(palabras)
    print(f"Palabras únicas: {unicas}")
    
    # Recuento
    recuento = {}
    for p in palabras:
        if p in recuento:
            recuento[p] += 1
        else:
            recuento[p] = 1
    print(f"Recuento: {recuento}")


    # ---EJERCICIO 6---
    print("\n--- EJERCICIO 6 ---")
    alumnos = {}
    
    print("Ingrese datos de 3 alumnos:")
    for i in range(3):
        nombre = input(f"Nombre del alumno {i+1}: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        # Guardamos las notas
        alumnos[nombre] = (n1, n2, n3)
        
    print("\nPromedios:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es: {promedio:.2f}")


    # ---EJERCICIO 7---
    print("\n--- EJERCICIO 7 ---")
    parcial_1 = {1, 2, 3, 4, 5}
    parcial_2 = {4, 5, 6, 7, 8}
    
    print(f"Aprobados P1: {parcial_1}")
    print(f"Aprobados P2: {parcial_2}")
    
    #  Aprobados P1 y P2
    ambos = parcial_1 & parcial_2
    print(f"Aprobaron ambos: {ambos}")
    
    # Aprobados solo uno
    solo_uno = parcial_1 ^ parcial_2
    print(f"Aprobaron solo uno de los dos: {solo_uno}")
    
    # Lista total sin repetir
    total = parcial_1 | parcial_2
    print(f"Total de aprobados (al menos uno): {total}")


    # ---EJERCICIO 8---
    print("\n--- EJERCICIO 8 ---")
    stock = {"lapiz": 10, "papel": 50}
    
    while True:
        opcion = input("\n1. Consultar | 2. Agregar Stock | 3. Nuevo Prod | 4. Salir: ")
        
        if opcion == "4":
            break
            
        prod = input("Producto: ").lower()
        
        if opcion == "1":
            print(f"Stock: {stock.get(prod, 'No existe')}")
        elif opcion == "2":
            if prod in stock:
                cant = int(input("Cantidad a sumar: "))
                stock[prod] += cant
                print(f"Nuevo stock: {stock[prod]}")
            else:
                print("El producto no existe (usá la opción 3).")
        elif opcion == "3":
            if prod not in stock:
                cant = int(input("Stock inicial: "))
                stock[prod] = cant
                print("Producto creado.")
            else:
                print("El producto ya existe (usá la opción 2).")


    # ---EJERCICIO 9---
    print("\n--- EJERCICIO 9 ---")
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés"
    }
    
    dia_c = input("Día a consultar (ej. lunes): ").lower()
    hora_c = input("Hora a consultar (ej. 10:00): ")
    
    evento = agenda.get((dia_c, hora_c), "Nada agendado")
    print(f"Evento: {evento}")


    # ---EJERCICIO 10---
    print("\n--- EJERCICIO 10 ---")
    paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "España": "Madrid"}
    print(f"Original: {paises}")
    
    invertido = {}
    for pais, capital in paises.items():
        invertido[capital] = pais
        
    print(f"Invertido: {invertido}")

if __name__ == "__main__":
    main()