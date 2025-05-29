cuentas = {}
peliculas = {}
menu_ok = True
print("Bienvenido al menú de gestión de actores y películas ")
while menu_ok:
    print("1) Crear cuenta ")
    print("2) Agregar/Editar/Eliminar películas")
    print("3) Agregar/Editar/Eliminar actores")
    print("4) Añadir actores a película")
    print("5) Votar por una película")
    opcion = int(input("Ingrese una opción "))
    match opcion:
        case 1:
            usuario = input("Ingrese el nombre de usuario ")
            if usuario in cuentas:
                print("Ya existe el usuario")
            else:
                contrasena = input(f"Ingrese la contraseña de {usuario} ")
                cuentas[usuario] = contrasena
        case 2:
            print("1) Agregar pelicula")
            print("2) Editar película")
            print("3) Eliminar películas")
            opcion_2 = int(input("Ingrese una opción "))
            match opcion_2:
                case 1:
                    pelicula = input("Ingrese la pelicula ")
                    if pelicula in peliculas:
                        print("La película ya existe")
                    else:
                        #agregar pelicula al diccionario
                        print(peliculas)
                case 2:
                    