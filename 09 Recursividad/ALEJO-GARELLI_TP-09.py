def calcular_factorial(n):
    # --- EJERCICIO 1 ---
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def fibonacci(n):
    # --- EJERCICIO 2 ---
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calcular_potencia(base, exponente):
    # --- EJERCICIO 3 ---
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

def decimal_a_binario(n):
    # --- EJERCICIO 4 ---
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra):
    # --- EJERCICIO 5 ---
    if len(palabra) < 2:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def suma_digitos(n):
    # --- EJERCICIO 6 ---
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    # --- EJERCICIO 7 ---
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    # --- EJERCICIO 8 ---
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        # 1 si el último dígito coincide, 0 si no
        es_igual = 1 if (numero % 10) == digito else 0
        return es_igual + contar_digito(numero // 10, digito)

# --- BLOQUE PRINCIPAL ---

if __name__ == "__main__":
    print("--- EJECUCIÓN DEL TRABAJO PRÁCTICO (1-8) ---")

    # 1. Factorial
    print("\n[Ejercicio 1] Factorial")
    try:
        n = int(input("Ingrese número para ver factoriales: "))
        for i in range(1, n + 1):
            print(f"{i}! = {calcular_factorial(i)}")
    except ValueError: print("Error: Ingrese un entero.")

    # 2. Fibonacci
    print("\n[Ejercicio 2] Fibonacci")
    try:
        n = int(input("Ingrese cantidad de términos: "))
        serie = [fibonacci(i) for i in range(n)]
        print(f"Serie: {serie}")
    except ValueError: print("Error: Ingrese un entero.")

    # 3. Potencia
    print("\n[Ejercicio 3] Potencia")
    try:
        b = int(input("Base: "))
        e = int(input("Exponente: "))
        print(f"Resultado: {calcular_potencia(b, e)}")
    except ValueError: print("Error: Ingrese enteros.")

    # 4. Binario
    print("\n[Ejercicio 4] Binario")
    try:
        n = int(input("Número decimal: "))
        if n >= 0: print(f"Binario: {decimal_a_binario(n)}")
        else: print("Debe ser positivo.")
    except ValueError: print("Error: Ingrese un entero.")

    # 5. Palíndromo
    print("\n[Ejercicio 5] Palíndromo")
    p = input("Ingrese palabra: ").lower()
    print(f"¿Es palíndromo? {es_palindromo(p)}")

    # 6. Suma Dígitos
    print("\n[Ejercicio 6] Suma de Dígitos")
    try:
        n = int(input("Ingrese número (ej. 1234): "))
        print(f"Suma: {suma_digitos(abs(n))}")
    except ValueError: print("Error: Ingrese un entero.")

    # 7. Bloques
    print("\n[Ejercicio 7] Pirámide de Bloques")
    try:
        n = int(input("Bloques en la base: "))
        print(f"Total necesario: {contar_bloques(n)}")
    except ValueError: print("Error: Ingrese un entero.")

    # 8. Contar Dígito
    print("\n[Ejercicio 8] Contar Dígito")
    try:
        num = int(input("Número completo: "))
        dig = int(input("Dígito a buscar (0-9): "))
        print(f"Apariciones: {contar_digito(num, dig)}")
    except ValueError: print("Error: Ingrese enteros.")