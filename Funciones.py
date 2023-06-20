# Elementos de una función
# Las funciones se escriben anteponiendo la palabra reservada def + el nombre de la función y entre () los parámetros si son requeridos. 
# El parámetro es un  dato de entrada y el return es uno de salida.
# Al final de la función siempre se llama a la palabra reservada return para devolver un dato. 
def nombre_función(parametro):
    # escribimos la funcionalidad utilizando el parámetro, en el caso de que se haya incorporado un parámetro.
    return parametro + 10

def saludar(nombre):
    if len(nombre) >= 5:
        return "Este " + nombre + " es un nombre largo"
    else:
        return nombre + " es un nombre corto"


    



nombre_completo = "Pepito Pistolero"

saludar("juan")
