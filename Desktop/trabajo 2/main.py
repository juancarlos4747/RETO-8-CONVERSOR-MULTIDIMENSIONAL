from monedas import cop_a_dolar, cop_a_euro, dolar_a_cop, euro_a_cop

from temperaturas import (
    celsius_a_fahrenheit,
    celsius_a_kelvin,
    fahrenheit_a_celsius,
    fahrenheit_a_kelvin,
    kelvin_a_celsius,
    kelvin_a_fahrenheit,
)

def mostrar_menu():
    print("\n" + "="*50)
    print("              PROGRAMA MODULAR")
    print("   Conversión de monedas")
    print("="*50)
    print("1. Monedas (Pesos colombianos <-> Dólares y Euros)")
    print("2. Temperaturas (Celsius, Fahrenheit, Kelvin)")
    print("3. Salir")
    return input("Elige una opción (1-3): ").strip()


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

def modulo_temperaturas():
    """Módulo interactivo para conversiones de temperatura."""
    print("\n--- Módulo de Temperaturas ---")
    print("Selecciona la conversión:")
    print("1) Celsius -> Fahrenheit")
    print("2) Celsius -> Kelvin")
    print("3) Fahrenheit -> Celsius")
    print("4) Fahrenheit -> Kelvin")
    print("5) Kelvin -> Celsius")
    print("6) Kelvin -> Fahrenheit")

    try:
        opcion = int(input("Elige opción (1-6): "))
        valor = float(input("Ingresa la temperatura: "))

        if opcion == 1:
            res = celsius_a_fahrenheit(valor)
            print(f"{valor:.2f} °C ≈ {res:.2f} °F")
        elif opcion == 2:
            res = celsius_a_kelvin(valor)
            print(f"{valor:.2f} °C ≈ {res:.2f} K")
        elif opcion == 3:
            res = fahrenheit_a_celsius(valor)
            print(f"{valor:.2f} °F ≈ {res:.2f} °C")
        elif opcion == 4:
            res = fahrenheit_a_kelvin(valor)
            print(f"{valor:.2f} °F ≈ {res:.2f} K")
        elif opcion == 5:
            res = kelvin_a_celsius(valor)
            print(f"{valor:.2f} K ≈ {res:.2f} °C")
        elif opcion == 6:
            res = kelvin_a_fahrenheit(valor)
            print(f"{valor:.2f} K ≈ {res:.2f} °F")
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
            modulo_temperaturas()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")

if __name__ == "__main__":
    main()