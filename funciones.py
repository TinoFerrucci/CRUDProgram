import os
from pathlib import Path, PureWindowsPath


'''Para este proyecto vamos a trabajar en D:\\Datos Basura\\Nueva Carpeta\\Recetas'''
path_inicial = "Receta"



def escribir_dentro_de_archivo():
    print("Escribe aquí debajo todo lo que quieras guardar (para salir solo introduzce un espacio en blanco):\n\n")
    texto = input("")
    lista_textos = []
    while texto != "":
        lista_textos.append(texto)
        texto = input("")
    return lista_textos


def crear_receta(nombre_arc, categoria):

    ruta = Path(path_inicial, categoria, nombre_arc + ".txt")
    print(f"Escribiendo la receta de {nombre_arc}")
    if ruta.exists():
        print("Nombre de Receta ya existente")
        if input("¿Deseas sobreescribir la receta? (si - no): ").lower() == "si":
            for linea in escribir_dentro_de_archivo():
                ruta.write_text(ruta.read_text() + "\n" + linea)
            print("Receta sobreescrito con éxito.")
    else:
        for linea in escribir_dentro_de_archivo():
            ruta.write_text("")
            ruta.write_text(ruta.read_text() + "\n" + linea)
        print("Receta creado con éxito.")


def crear_categoria(nombre_cat):
    ruta = Path(path_inicial, nombre_cat)
    if ruta.exists():
        print("Categoría ya existente.")
    else:
        os.mkdir(ruta)
        print("Categoría creada con éxito.")


def elegir_receta(nombre_arc, categoria):
    ruta = Path(path_inicial, categoria, nombre_arc + ".txt")
    if ruta.exists():
        print(f"Mostrando la receta de {nombre_arc}\n")
        leer_receta(ruta)
    else:
        print("Esa receta no existe")


def elegir_categoria(nombre_cat):
    ruta = Path(path_inicial, nombre_cat)
    if ruta.exists():
        print(f"Ingresando a {nombre_cat}")
        path = ruta
    else:
        print("La categoria no existe")


def eliminar_receta(nombre_arc, categoria):
    ruta = Path(path_inicial, categoria, nombre_arc + ".txt")
    if ruta.exists():
        os.remove(ruta)
        print("Receta eliminado correctamente")
    else:
        print("Receta inexistente.")


def eliminar_categoria(nombre_cat):
    ruta = Path(path_inicial, nombre_cat)
    if ruta.exists():
        if contar_cantidad_recetas_en_categoria(ruta) == 0:
            os.rmdir(ruta)
            print("Categoria eliminada correctamente.")
        else:
            print("Categoria aún con recetas.")
    else:
        print("Imposible de eliminar una categoria inexistente.")


def menu():
    archivo_abierto = Path('menu.txt')
    print(archivo_abierto.read_text())


def volver_inicio(path):
    path = path.parent


def volver_inicio_receta(path):
    path = path.parent.parent


def limpiar_pantalla():
    os.system('cls')


def contar_cantidad_recetas_total():
    total_recetas = 0
    lista = lista_categorias()
    for categoria in lista:
        total_recetas += contar_cantidad_recetas_en_categoria(categoria)
    return total_recetas


def lista_categorias():
    lista = []
    cant_cat = contar_cantidad_categorias()
    for path in Path(path_inicial).iterdir():
        if path.is_dir():
            lista.append(path)
    return lista


def contar_cantidad_recetas_en_categoria(ruta):
    initial_count = 0
    for path in Path(ruta).iterdir():
        if path.exists():
            initial_count += 1
    return initial_count

def contar_cantidad_categorias():
    initial_count = 0
    for path in Path(path_inicial).iterdir():
        if path.is_dir():
            initial_count += 1
    return initial_count


def mostrar_recetas(categoria):
    lista = []
    ruta = Path(path_inicial, categoria)
    cant_recetas = contar_cantidad_recetas_en_categoria(ruta)
    print(f"Hay {cant_recetas} recetas de la categoria {categoria} para elegir:\n")
    for path in ruta.iterdir():
        if path.is_file():
            lista.append(path)
    for path in lista:
        print(path.stem)


def mostrar_categorias():
    lista = []
    cant_cat = contar_cantidad_categorias()
    print(f"Hay {cant_cat} categorias para elegir:\n")
    for path in Path(path_inicial).iterdir():
        if path.is_dir():
            lista.append(path)
    for path in lista:
        print(path.stem)


def leer_receta(ruta_receta):
    a = open(ruta_receta)
    for i in a:
        print(i)
    a.close()


def salto_de_linea():
    print("\n")
