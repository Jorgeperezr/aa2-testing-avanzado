"""
Conjunto mejorado de pruebas - cobertura completa (sentencias y ramas). Agrega casos de elemento no encontrado y validacion de entrada invalida.
"""
import pytest
from binary_search import binary_search

LISTA = [2, 5, 8, 12, 16, 23, 38, 45, 67, 99]

# --- Casos donde el elemento SI existe (cubre la rama de exito) ---
def test_encuentra_primer_elemento():
    assert binary_search(LISTA, 2) == 0

def test_encuentra_ultimo_elemento():
    assert binary_search(LISTA, 99) == 9

def test_encuentra_elemento_central():
    assert binary_search(LISTA, 16) == 4

def test_encuentra_elemento_intermedio():
    assert binary_search(LISTA, 38) == 6

# --- Casos donde el elemento NO existe (cubre la rama del return -1, linea 36) ---
def test_elemento_inexistente():
    assert binary_search(LISTA, 100) == -1

def test_elemento_menor_que_minimo():
    assert binary_search(LISTA, 1) == -1

def test_elemento_mayor_que_maximo():
    assert binary_search(LISTA, 200) == -1

def test_lista_vacia():
    assert binary_search([], 5) == -1

# --- Casos de validacion de entrada (cubre la rama del TypeError, linea 22) ---
def test_argumento_no_es_lista_lanza_error():
    with pytest.raises(TypeError):
        binary_search("no-es-lista", 5)

def test_argumento_none_lanza_error():
    with pytest.raises(TypeError):
        binary_search(None, 5)