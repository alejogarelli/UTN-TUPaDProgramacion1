#Ejercicio 1...

print("Hola Mundo!")

#Ejercicio 2...

nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3...

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Edad: ")
residencia = input("¿Donde vives?: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4...

radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"Dado el radio del circulo ingresado, el area es {area} y el perimetro es {perimetro}")

#Ejercicio 5...

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos * (1 / 3600)
print(f"Equivalen a {horas} horas")

#Ejercicio 6...

num = int(input("Ingrese un numero: "))
print(f"La tabla de {num} es: 1= {num * 1} 2= {num * 2} 3= {num * 3} 4= {num * 4} 5= {num * 5} 6= {num * 6} 7= {num * 7} 8= {num * 8} 9= {num * 9}")

#Ejercicio 7...

num1 = int(input("Ingrese un numero entero distinto de 0: "))
num2 = int(input("Ingrese otro numero entero distinto de 0: "))
print(f"Suma = {num1 + num2} Resta = {num1 - num2} Division = {num1 / num2} Multiplicacion {num1 * num2}")

#Ejercicio 8...

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso: "))
print(f"Tu indice de masa corporal es: {peso / (altura ** 2)}")

#Ejercicio 9...

temp = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"La temperatura en Fahrenheit es: {(9/5) * temp + 32}")

#Ejercicio 10...

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
print(f"El promedio de los tres numero es: {(num1 + num2 + num3) / 3}")