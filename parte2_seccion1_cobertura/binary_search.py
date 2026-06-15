"""
UIDE - Diseño de Pruebas, Control de Calidad y Mantenimiento.
Algoritmo de busqueda binaria iterativa sobre una lista ordenada ascendentemente.
"""


def binary_search(arr, target):
    """
    Busca un valor objetivo en una lista ordenada de forma ascendente.

    Args:
        arr (list): Lista de numeros ordenada ascendentemente.
        target (int): Valor a buscar.

    Returns:
        int: Indice del elemento encontrado, o -1 si no existe.

    Raises:
        TypeError: Si el primer argumento no es una lista.
    """
    if not isinstance(arr, list):
        raise TypeError("El primer argumento debe ser una lista.")

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
    