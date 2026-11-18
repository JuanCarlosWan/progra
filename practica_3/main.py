# main.py: programa principal con los menús
from matriz import MatrizFloat  # importa la clase de matrices (faltaba en la versión anterior)
from utils import leer_int, crear_menu  # importa las funciones de lectura y menú (faltaban)

OPCIONES_PRINCIPAL = [  # lista con las opciones del menú principal
    "Construir matriz 1D",  # opción 1
    "Construir matriz 2D",  # opción 2
    "Construir matriz identidad",  # opción 3
    "Introducir matriz",  # opción 4
    "Mostrar matriz",  # opción 5
    "Operaciones con matrices",  # opción 6
    "Terminar",  # opción 7
]  # fin de la lista

OPCIONES_OPERACIONES = [  # lista con las opciones del submenú de operaciones
    "Sumar matrices",  # opción 1
    "Restar matrices",  # opción 2
    "Volver al menú principal",  # opción 3
]  # fin de la lista


def submenu_operaciones(matriz):  # muestra el submenú de sumar/restar
    """Repite el submenú hasta que el usuario elija volver."""
    if not matriz.existe():  # si todavía no hay matriz principal...
        print("Primero debe crear la matriz (opciones 1, 2 o 3).")  # ...avisa
        return  # y vuelve al menú principal
    while True:  # repite el submenú hasta que se elija volver
        opcion = crear_menu(OPCIONES_OPERACIONES)  # muestra el submenú y lee la opción
        if opcion == 3:  # si elige "Volver al menú principal"...
            return  # ...sale del submenú
        try:  # intenta hacer la operación (puede haber errores de dimensiones)
            print("Datos de la segunda matriz:")  # indica que ahora se pide la segunda matriz
            segunda = MatrizFloat()  # crea un objeto vacío para la segunda matriz
            segunda.crear_matriz2D(leer_int("Número de filas: "), leer_int("Número de columnas: "))  # pide su tamaño y la crea
            if not MatrizFloat.mismas_dimensiones(matriz, segunda):  # comprueba el tamaño antes de pedir los valores
                print("Error: las dimensiones de ambas matrices deben coincidir.")  # avisa si no coinciden
                continue  # vuelve a mostrar el submenú
            segunda.introducir()  # pide los valores de la segunda matriz
            if opcion == 1:  # si eligió sumar...
                resultado = matriz.sumar_matrices(segunda)  # ...suma las dos matrices
                print("Resultado de la suma:")  # muestra el título del resultado
            else:  # si eligió restar...
                resultado = matriz.restar_matrices(segunda)  # ...resta las dos matrices
                print("Resultado de la resta:")  # muestra el título del resultado
            resultado.mostrar()  # muestra la matriz resultado
        except ValueError as error:  # si algo falló (p. ej. dimensiones <= 0)...
            print(f"Error: {error}")  # ...muestra el mensaje de error


def main():  # función principal del programa
    """Repite el menú principal hasta que el usuario elija terminar."""
    matriz = MatrizFloat()  # crea la matriz principal vacía
    while True:  # repite el menú hasta elegir "Terminar"
        opcion = crear_menu(OPCIONES_PRINCIPAL)  # muestra el menú principal y lee la opción
        try:  # intenta ejecutar la opción (puede lanzar ValueError)
            if opcion == 1:  # construir matriz 1D
                matriz = MatrizFloat()  # crea un objeto nuevo
                matriz.crear_matriz1D(leer_int("Número de elementos: "))  # pide el tamaño y crea la matriz 1D
                print("Matriz 1D creada.")  # confirma la creación
            elif opcion == 2:  # construir matriz 2D
                matriz = MatrizFloat()  # crea un objeto nuevo
                matriz.crear_matriz2D(leer_int("Número de filas: "), leer_int("Número de columnas: "))  # pide filas y columnas y la crea
                print("Matriz 2D creada.")  # confirma la creación
            elif opcion == 3:  # construir matriz identidad
                matriz = MatrizFloat.matriz_identidad(leer_int("Tamaño n de la matriz identidad: "))  # pide n y crea la identidad
                print("Matriz identidad creada.")  # confirma la creación
            elif opcion == 4:  # introducir valores
                matriz.introducir()  # pide los valores de cada posición
            elif opcion == 5:  # mostrar matriz
                matriz.mostrar()  # muestra la matriz por pantalla
            elif opcion == 6:  # operaciones
                submenu_operaciones(matriz)  # abre el submenú de sumar/restar
            else:  # opción 7: terminar
                print("Hasta pronto.")  # mensaje de despedida
                break  # sale del bucle y termina el programa
        except ValueError as error:  # si alguna opción lanzó un error...
            print(f"Error: {error}")  # ...muestra el mensaje y sigue con el menú


if __name__ == "__main__":  # solo si se ejecuta este archivo directamente (faltaba antes)...
    main()  # ...arranca el programa
