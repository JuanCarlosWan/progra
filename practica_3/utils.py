# utils.py: funciones para leer datos del teclado y mostrar menús


def leer_int(mensaje="Introduce un número entero: "):  # define la función que lee un entero
    """Lee un número entero del teclado. Si no es válido, lo vuelve a pedir."""
    while True:  # repite hasta que el usuario escriba un entero válido
        try:  # intenta convertir lo escrito a entero
            return int(input(mensaje))  # muestra el mensaje, lee el texto, lo pasa a int y lo devuelve
        except ValueError:  # si el texto no era un entero, int() lanza ValueError
            print("Entrada no válida. Debe ser un número entero.")  # avisa del error y vuelve a pedirlo


def leer_float(mensaje="Introduce un número decimal: "):  # define la función que lee un decimal
    """Lee un número decimal del teclado. Si no es válido, lo vuelve a pedir."""
    while True:  # repite hasta que el usuario escriba un decimal válido
        try:  # intenta convertir lo escrito a decimal
            return float(input(mensaje))  # muestra el mensaje, lee el texto, lo pasa a float y lo devuelve
        except ValueError:  # si el texto no era un número, float() lanza ValueError
            print("Entrada no válida. Debe ser un número decimal.")  # avisa del error y vuelve a pedirlo


def crear_menu(opciones_menu):  # define la función que muestra un menú y devuelve la opción elegida
    """Muestra las opciones numeradas desde 1 y devuelve el número elegido (int)."""
    print()  # deja una línea en blanco antes del menú
    for numero, opcion in enumerate(opciones_menu, start=1):  # recorre las opciones numerándolas desde 1
        print(f"{numero}. {opcion}")  # imprime cada opción con su número delante
    while True:  # repite hasta que se elija una opción que exista
        seleccion = leer_int("Seleccione una opción: ")  # pide al usuario un número entero
        if 1 <= seleccion <= len(opciones_menu):  # comprueba que el número está dentro del rango del menú
            return seleccion  # si es válido, lo devuelve
        print(f"Opción no válida. Elija un número entre 1 y {len(opciones_menu)}.")  # si no, avisa y repite
