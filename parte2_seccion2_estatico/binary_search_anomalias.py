"""
UIDE - Diseño de Pruebas, Control de Calidad y Mantenimiento.
Algoritmo de busqueda binaria CON anomalias de flujo de datos introducidas intencionalmente para el analisis estatico con pylint.
"""
def binary_search(arr, target):
    """
    Busca un valor objetivo en una lista ordenada de forma ascendente.
    Esta version contiene anomalias de flujo de datos a proposito.
    """
    if not isinstance(arr, list):
        raise TypeError("El primer argumento debe ser una lista.")

    # ANOMALIA 1 (DU - Define-Unused): 'contador' se define pero nunca se usa.
    contador = 0

    # ANOMALIA 2 (DU - Define-Unused): 'estado_busqueda' se define pero nunca se usa.
    estado_busqueda = "pendiente"

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
    