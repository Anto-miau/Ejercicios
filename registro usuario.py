usuarios = {}
sexos = ['F', 'M']
def ingresar_usuario():
    print("--Ingresar usuario--")
    nombre = input("Ingrese el nombre de usuario: ")

    if nombre in usuarios:
        print("Ya existe un usuario con ese nombre.")
        return

    sexo = input("Ingrese sexo (F o M): ")

    if sexo not in (sexos):
        print("Sexo no válido.")
        return
    
    if sexo == 'f' or sexo == 'F':
        sexo = 'F'
    elif sexo == 'm' or sexo == 'M':
        sexo = 'M'

    contraseña = input("Ingrese contraseña: ")

    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return

    for c in contraseña:
        if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
            break
    else:
        print("La contraseña debe tener al menos una letra.")
        return

    if ' ' in contraseña:
        print("La contraseña no puede contener espacios.")
        return

    usuarios[nombre] = {'sexo': sexo, 'contraseña': contraseña}
    print("✅ Usuario ingresado exitosamente.")

def buscar_usuario():
    print("--Buscar usuario--")
    nombre = input("Ingrese el nombre de usuario a buscar: ")

    if nombre in usuarios:
        datos = usuarios[nombre]
        print(f"Sexo: {datos['sexo']}")
        print(f"Contraseña: {datos['contraseña']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    print("--Eliminar usuario--")
    nombre = input("Ingrese el nombre de usuario a eliminar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado")
    else:
        print("No se pudo eliminar usuario")

def main():
    while True:
        print("\n📋 Menú Principal")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")

        try:
            op = int(input("Seleccione una opción: "))
            if op == 1:
                ingresar_usuario()
            elif op == 2:
                buscar_usuario()
            elif op == 3:
                eliminar_usuario()
            elif op == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!")
        except:
            print("Debe ingresar una opción válida!!")

if __name__ == '__main__':
    main()
