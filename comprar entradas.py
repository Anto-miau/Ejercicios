compradores = {}

def comprar_entrada():
    print("comprar entrada")
    nombre = input("nombre: ").strip()
    if nombre in compradores:
        print("ya esta este comprador")
        return

    print("g (general), v (vip)")
    tipo = input("entrada: ").strip()
    if tipo not in ('g', 'v'):
        print("opcion no valida")
        return

    codigo = input("codigo: ")

    if len(codigo) < 6:
        print("debe tener 6 o mas caracteres")
        return

    for i in codigo:
        if i >= '0' and i <= '9':
            break
    else:
        print("El código debe tener al menos un número.")
        return

    for i in codigo:
        if i >= 'A' and i <= 'Z':
            break
    else:
        print("El código debe tener al menos una letra mayúscula.")
        return

    for i in codigo:
        if i == ' ':
            print("El código no puede contener espacios.")
            return

    compradores[nombre] = {'tipo': tipo, 'codigo': codigo}
    print("entrada registrada con éxito")

def consultar_comprador():
    print("consultar comprador")
    nombre = input("nombre: ")
    if nombre in compradores:
        tipo = compradores[nombre]['tipo']
        codigo = compradores[nombre]['codigo']
        print(f"tipo de entrada: {tipo}")
        print(f"código de confirmación: {codigo}")
    else:
        print("el comprador no se encuentra")

def cancelar_compra():
    print("cancelar compra")
    nombre = input("nombre: ")
    if nombre in compradores:
        del compradores[nombre]
        print("¡compra cancelada!")
    else:
        print("no se pudo cancelar la compra")

def main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Comprar entrada")
        print("2. Consultar comprador")
        print("3. Cancelar compra")
        print("4. Salir")

        try:
            op = int(input("elige una opción: "))
            if op == 1:
                comprar_entrada()
            elif op == 2:
                consultar_comprador()
            elif op == 3:
                cancelar_compra()
            elif op == 4:
                print("Programa terminado...")
                break
            else:
                print("debe ingresar una opción válida!!")
        except:
            print("error")

if __name__ == '__main__':
    main()

