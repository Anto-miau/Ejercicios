compradores = {}
def comprar_entrada():
    print("\n -- comprar entrada--")
    nombre = input("nombre: ").strip()
    if nombre in compradores:
        print("ya esta este comprador")
        return
    print("g (general), v(vip)")
    tipo = input("entrada: ").strip()
    if tipo == 'g':
        compradores[nombre] = 'g'
    elif tipo == 'v':
        compradores[nombre] = 'v'
    else:
        print("opcion no valida")
    
    codigo = input("codigo: ")
    if len(codigo) < 6:
        print("debe tener 6 o mas caracteres")
        return
    for c in codigo:
        if c >= '0' and c <= '9':
            break
    else:
        print("⚠️ El código debe tener al menos un número.")
        return
    for c in codigo:
        if c >= 'A' and c <= 'Z':
            break
    else:
        print("⚠️ El código debe tener al menos una letra mayúscula.")
        return
    if ' ' in codigo:
        print("⚠️ El código no puede contener espacios.")
        return
def consultar_comprador():
    print("--Consultar comprador--")
    nombre = input("Ingrese el nombre a consultar: ")

    if nombre in compradores:
        tipo = compradores[nombre]['tipo']
        codigo = compradores[nombre]['codigo']
        print(f"Tipo de entrada: {tipo}")
        print(f"Código de confirmación: {codigo}")
    else:
        print("El comprador no se encuentra.")

def cancelar_compra():
    print("--Cancelar compra--")
    nombre = input("Ingrese el nombre del comprador a cancelar: ")

    if nombre in compradores:
        del compradores[nombre]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la compra.")

def main():
    while True:
        print("\n📋 Menú Principal")
        print("1. Comprar entrada")
        print("2. Consultar comprador")
        print("3. Cancelar compra")
        print("4. Salir")

        try:
            op = int(input("Seleccione una opción: "))
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
                print("Debe ingresar una opción válida!!")
        except:
            print("Debe ingresar una opción válida!!")

if __name__ == '__main__':
    main()