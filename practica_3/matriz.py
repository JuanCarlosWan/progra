# matriz.py: clase MatrizFloat
import numpy as np  # importa numpy para trabajar con matrices

from utils import leer_float  # importa la función que lee decimales (faltaba en la versión anterior)


class MatrizFloat:  # define la clase que representa una matriz 1D/2D de decimales
    """
    Matriz dinámica 1D/2D.
    Atributo de clase: TIPO_DATO (np.float32).
    Atributos de instancia: _matriz (numpy), _nfil (int), _ncol (int).
    """

    TIPO_DATO = np.float32  # atributo de clase: tipo de dato que usarán todas las matrices

    def __init__(self):  # método de instancia: se ejecuta al crear un objeto nuevo
        """Inicializa la matriz a None y las filas y columnas a 0."""
        self._matriz = None  # todavía no hay matriz creada
        self._nfil = 0  # número de filas inicial
        self._ncol = 0  # número de columnas inicial

    @classmethod  # método de clase: recibe la clase (cls) en vez de un objeto
    def matriz_identidad(cls, n):  # constructor alternativo que crea una matriz identidad n x n
        """Crea y devuelve una nueva MatrizFloat identidad de tamaño n x n."""
        nueva = cls()  # crea un objeto vacío de la clase
        nueva.crear_matriz2D(n, n)  # le crea una matriz de ceros n x n (y valida n)
        nueva._matriz = np.eye(n, dtype=cls.TIPO_DATO)  # la sustituye por la identidad (unos en la diagonal)
        return nueva  # devuelve el objeto creado

    @staticmethod  # método estático: no usa ni self ni cls
    def mismas_dimensiones(m1, m2):  # compara las dimensiones de dos matrices
        """Devuelve True si m1 y m2 tienen las mismas filas y columnas, False si no."""
        return m1._nfil == m2._nfil and m1._ncol == m2._ncol  # True solo si coinciden filas y columnas

    def crear_matriz2D(self, n_fil, n_col):  # crea una matriz de ceros con n_fil filas y n_col columnas
        """Crea una matriz 2D de ceros con las filas y columnas indicadas."""
        if n_fil < 1 or n_col < 1:  # comprueba que las dimensiones sean mayores que 0
            raise ValueError("Las dimensiones deben ser mayores que 0.")  # si no, lanza un error
        self._matriz = np.zeros((n_fil, n_col), dtype=self.TIPO_DATO)  # crea la matriz llena de ceros
        self._nfil = n_fil  # guarda el número de filas
        self._ncol = n_col  # guarda el número de columnas

    def crear_matriz1D(self, n_elementos):  # crea una matriz de una sola fila
        """Crea una matriz 1D de ceros (1 fila y n_elementos columnas)."""
        self.crear_matriz2D(1, n_elementos)  # reutiliza crear_matriz2D con 1 fila

    def existe(self):  # comprueba si la matriz ya se ha creado
        """Devuelve True si la matriz está creada, False si no."""
        return self._matriz is not None  # está creada si _matriz ya no es None

    def introducir(self):  # pide por teclado todos los valores de la matriz
        """Pide un valor decimal para cada posición (i, j). Error si la matriz no existe."""
        if not self.existe():  # si la matriz no está creada...
            raise ValueError("Primero debe crear la matriz.")  # ...lanza un error
        for i in range(self._nfil):  # recorre cada fila
            for j in range(self._ncol):  # recorre cada columna de esa fila
                self._matriz[i, j] = leer_float(f"Valor para la posición ({i}, {j}): ")  # pide y guarda el valor

    def mostrar(self):  # muestra la matriz por pantalla
        """Muestra las dimensiones y los elementos, o un aviso si no existe."""
        if not self.existe():  # si la matriz no está creada...
            print("La matriz no existe. Cree una matriz primero.")  # ...avisa
            return  # y sale del método sin mostrar nada más
        print(f"Dimensiones: {self._nfil} x {self._ncol}")  # muestra filas x columnas
        print(self._matriz)  # muestra los elementos de la matriz

    def sumar_matrices(self, otra_matriz):  # suma esta matriz con otra
        """Devuelve una nueva MatrizFloat con la suma. Error si las dimensiones no coinciden."""
        if not MatrizFloat.mismas_dimensiones(self, otra_matriz):  # comprueba que tengan el mismo tamaño
            raise ValueError("Las dimensiones de las matrices no coinciden.")  # si no, lanza un error
        resultado = MatrizFloat()  # crea un objeto nuevo para el resultado
        resultado.crear_matriz2D(self._nfil, self._ncol)  # le da el mismo tamaño que las matrices
        resultado._matriz = self._matriz + otra_matriz._matriz  # guarda la suma elemento a elemento
        return resultado  # devuelve la matriz resultado

    def restar_matrices(self, otra_matriz):  # resta otra matriz a esta
        """Devuelve una nueva MatrizFloat con la resta. Error si las dimensiones no coinciden."""
        if not MatrizFloat.mismas_dimensiones(self, otra_matriz):  # comprueba que tengan el mismo tamaño
            raise ValueError("Las dimensiones de las matrices no coinciden.")  # si no, lanza un error
        resultado = MatrizFloat()  # crea un objeto nuevo para el resultado
        resultado.crear_matriz2D(self._nfil, self._ncol)  # le da el mismo tamaño que las matrices
        resultado._matriz = self._matriz - otra_matriz._matriz  # guarda la resta elemento a elemento
        return resultado  # devuelve la matriz resultado
