from Sexto_Proyecto_Funciones import *

menu()
numero = int(input("Ingrese una opcion: "))
while numero not in range(1,7):
    numero = int(input("Ingrese una opcion Valida: "))

while numero != 6:
    if numero == 1:
        limpiar_pantalla()
        mostrar_categorias()
        salto_de_linea()
        categoria = input("Ingrese la categoria a la que quiere acceder: ").capitalize()
        if Path(path_inicial,categoria).exists():
            elegir_categoria(categoria)
            if contar_cantidad_recetas_en_categoria(Path(path_inicial, categoria)) > 0:
                limpiar_pantalla()
                mostrar_recetas(categoria)
                salto_de_linea()
                receta = input("Ingrese el nombre de la receta la cual quiere ver: ").capitalize()
                limpiar_pantalla()
                elegir_receta(receta, categoria)
            else:
                salto_de_linea()
                print(f"No se pueden elegir recetas dentro de {categoria} ya que no existe ninguna")
        else:
            salto_de_linea()
            print(f"No existe la categoría {categoria}.")
    elif numero == 2:
        limpiar_pantalla()
        mostrar_categorias()
        salto_de_linea()
        categoria = input("Ingrese la categoria a la que quiere acceder: ").capitalize()
        if Path(path_inicial,categoria).exists():
            elegir_categoria(categoria)
            limpiar_pantalla()
            mostrar_recetas(categoria)
            salto_de_linea()
            receta = input("Ingrese el nombre de la receta la cual quiere crear: ").capitalize()
            limpiar_pantalla()
            crear_receta(receta, categoria)
        else:
            salto_de_linea()
            print(f"No existe la categoría {categoria}.")
    elif numero == 3:
        mostrar_categorias()
        salto_de_linea()
        categoria = input("Ingrese la categoria que quiere crear: ").capitalize()
        crear_categoria(categoria)
    elif numero == 4:
        mostrar_categorias()
        salto_de_linea()
        categoria = input("Ingrese la categoria a la que quiere acceder: ").capitalize()
        limpiar_pantalla()
        if Path(path_inicial, categoria).exists():
            elegir_categoria(categoria)
            if contar_cantidad_recetas_en_categoria(Path(path_inicial, categoria)) > 0:
                mostrar_recetas(categoria)
                receta = input("Ingrese el nombre de la receta que quiera borrar: ").capitalize()
                eliminar_receta(receta, categoria)
            else:
                salto_de_linea()
                print(f"No se pueden eliminar recetas dentro de {categoria} ya que no existe ninguna")
        else:
            salto_de_linea()
            print(f"No existe la categoría {categoria}.")
    elif numero == 5:
        mostrar_categorias()
        categoria = input("Ingrese la categoria que quiere eliminar: ").capitalize()
        eliminar_categoria(categoria)
    input("\n\nPRESIONE ENTER PARA VOLVER AL MENU INICIAL")
    limpiar_pantalla()
    menu()
    numero = int(input("Ingrese una opcion: "))
    while numero not in range(1, 7):
        numero = int(input("Ingrese una opcion Valida: "))


print("Programa terminado")