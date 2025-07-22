def mostrar_menu():
    print("\nCalculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def solicitar_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingrese números válidos.")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '5':
            print("👋 Saliendo de la calculadora. ¡Hasta luego!")
            break

        if opcion not in {'1', '2', '3', '4'}:
            print("❌ Opción inválida. Intente nuevamente.")
            continue

        num1, num2 = solicitar_numeros()

        if opcion == '1':
            resultado = num1 + num2
            print(f"🟢 Resultado: {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"🟢 Resultado: {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"🟢 Resultado: {num1} * {num2} = {resultado}")
        elif opcion == '4':
            if num2 == 0:
                print("⚠️ Error: División por cero no permitida.")
            else:
                resultado = num1 / num2
                print(f"🟢 Resultado: {num1} / {num2} = {resultado}")

if __name__ == "__main__":
    calculadora()
