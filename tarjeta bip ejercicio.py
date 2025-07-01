tarjetas = {}
def comprar_tarjeta():
    print("comprar tarjeta bip")
    nombre = input("nombre: ").strip()
    if nombre in tarjetas:
        print("tarjeta ya registrada")
    else:
        tarjetas[nombre] = 750
        print("tarjeta registrada con saldo inicial, 750")
def recargar_tarjeta():
    print("recargar tarjeta")
    nombre = input("nombre: ")
    if nombre in tarjetas:
        try:
            monto = int(input("monto: "))
            if monto > 0 and monto % 100 == 0:
                tarjetas[nombre] += monto
                print(f"monto añadido "[monto])
            else:
                print("monto invalido")
        except ValueError:
            print("error")
    else:
        print("no existe")
def mostrar_estado():
    if not tarjetas:
        print("no hay tarjetas")
    else:
        total_saldo = 0
        for nombre, saldo in tarjetas.items():
            print(f"{nombre}: {saldo}")
            total_saldo += saldo
        print(f"total de tarjetas: {len(tarjetas)}")
        print(f"promedio saldos: {total_saldo / len(tarjetas)}")
def main():
    while True:
        print("\nMENU PRINCIPAL METRO DE SANTIAGO")
        print("1.- Comprar tarjeta Bip.")
        print("2.- Recargar tarjeta.")
        print("3.- Mostrar estado de tarjetas.")
        print("4.- Salir.")

        try:
            op = int(input("eliga opcion: "))
            if op == 1:
                comprar_tarjeta()
            elif op == 2:
                recargar_tarjeta()
            elif op == 3:
                mostrar_estado()
            elif op == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("error")
if __name__ == "__main__":
    main()
