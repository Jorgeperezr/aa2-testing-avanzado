"""
Conjunto INICIAL de pruebas - cobertura parcial.
Solo prueba casos donde el elemento SI existe en la lista.
"""
from binary_search import binary_search

LISTA = [2, 5, 8, 12, 16, 23, 38, 45, 67, 99]


def test_encuentra_primer_elemento():
    assert binary_search(LISTA, 2) == 0


def test_encuentra_ultimo_elemento():
    assert binary_search(LISTA, 99) == 9


def test_encuentra_elemento_central():
    assert binary_search(LISTA, 16) == 4
    