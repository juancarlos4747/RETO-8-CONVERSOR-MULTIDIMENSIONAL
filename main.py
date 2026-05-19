from monedas import cop_a_dolar, cop_a_euro, dolar_a_cop, euro_a_cop

def mostrar_menu():
    print("\n" + "="*50)
    print("              PROGRAMA MODULAR")
    print("   Conversión de monedas")
    print("="*50)
    print("1. Monedas (Pesos colombianos <-> Dólares y Euros)")
    print("2. Salir")
    return input("Elige una opción (1-2): ").strip()


def modulo_monedas():
    print("\n--- Módulo de Monedas ---")
    print("Selecciona el tipo de conversión:")
    print("a) Pesos colombianos -> Dólares")
    print("b) Pesos colombianos -> Euros")
    print("c) Dólares -> Pesos colombianos")
    print("d) Euros -> Pesos colombianos")

    opcion = input("Opción (a/b/c/d): ").strip().lower()

    try:
        valor = float(input("Ingresa el monto: "))

        if opcion == "a":
            res = cop_a_dolar(valor)
            print(f"{valor:.2f} COP ≈ {res:.2f} USD")
        elif opcion == "b":
            res = cop_a_euro(valor)
            print(f"{valor:.2f} COP ≈ {res:.2f} EUR")
        elif opcion == "c":
            res = dolar_a_cop(valor)
            print(f"{valor:.2f} USD ≈ {res:.2f} COP")
        elif opcion == "d":
            res = euro_a_cop(valor)
            print(f"{valor:.2f} EUR ≈ {res:.2f} COP")
        else:
            print("Opción no válida.")

    except ValueError:
        print("Error: debes ingresar un número válido.")

def main():
    print("Bienvenido al programa modular de conversiones!")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            modulo_monedas()
        elif opcion == "2":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Elige 1 o 2.")

if __name__ == "__main__":
    main()