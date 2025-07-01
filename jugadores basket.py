jugadores = {}
partidos = {'f1': 50, 'f2': 60}
def registro_jugador():
    print("--registro de jugador--")
    nombre = input("ingrese nombre: ").strip()
    if nombre in jugadores:
        print("jugador ya existente")
    else:
        print("partidos")
        print(f"estrellas (max50), quedan {50 - partidos['F1']}")
        print(f"tigres (max60), quedan {60 - partidos['f2']} ")
    try:
        opcion = int(input("¿A qué partido desea asistir?: "))
        if opcion == 1:
            if partidos["F1"] < 50:
                jugadores[nombre] = 'F1'
                partidos['F1'] += 1
        elif opcion == 2:
            if partidos['f2'] < 60:
                jugadores[nombre] = 'F2'
                partidos['F2'] += 1
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: Debes ingresar un número")
def main():
    while True:
        print("--Menú--")
        print("1. Registrar jugador")
        print("2. Salir")
        try:
            op = int(input("Ingrese la opción: "))
            if op == 1:
                registro_jugador()
            elif op == 2:
                print("Saliendo...")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Error: ingrese un número válido")

if __name__ == '__main__':
    main()