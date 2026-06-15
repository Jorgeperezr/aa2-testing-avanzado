"""
UIDE - Diseño de Pruebas, Control de Calidad y Mantenimiento
Pruebas unitarias sobre los casos generados por pairwise testing.
Valida las reglas de negocio del Sistema de Reserva de Vuelos.
"""
import pytest
from allpairspy import AllPairs

# Mismos factores del generador
FACTORES = {
    "Ciudad_Origen": ["Quito", "Guayaquil", "Cuenca", "Madrid", "Bogota"],
    "Ciudad_Destino": ["Lima", "Madrid", "Miami", "Panama", "Buenos_Aires"],
    "Franja_Horaria": ["Madrugada", "Manana", "Mediodia", "Tarde", "Noche"],
    "Clase_Cabina": ["Economica", "Ejecutiva"],
    "Tipo_Pasajero": ["Adulto", "Nino", "Tercera_Edad"],
}

FRANJAS_VALIDAS = FACTORES["Franja_Horaria"]

def validar_reserva(origen, destino, franja, clase, pasajero):
    """
    Valida una reserva de vuelo segun las reglas de negocio. Retorna (True, "OK") si es valida, o (False, motivo) si no lo es.
    """
    if origen == destino:
        return False, "Origen y destino no pueden ser iguales"
    if pasajero == "Nino" and clase == "Ejecutiva":
        return False, "Un nino no puede viajar solo en clase Ejecutiva"
    if franja not in FRANJAS_VALIDAS:
        return False, "Franja horaria invalida"
    return True, "OK"

# Generar la lista de casos pairwise una sola vez
NOMBRES = list(FACTORES.keys())
VALORES = list(FACTORES.values())
CASOS = list(AllPairs(VALORES))

@pytest.mark.parametrize("caso", CASOS)
def test_franja_horaria_valida(caso):
    """Cada caso debe tener una franja horaria dentro del conjunto valido."""
    datos = dict(zip(NOMBRES, caso))
    assert datos["Franja_Horaria"] in FRANJAS_VALIDAS

@pytest.mark.parametrize("caso", CASOS)
def test_validacion_no_lanza_excepcion(caso):
    """La funcion de validacion debe ejecutarse sin errores en todos los casos."""
    datos = dict(zip(NOMBRES, caso))
    resultado, _ = validar_reserva(
        datos["Ciudad_Origen"],
        datos["Ciudad_Destino"],
        datos["Franja_Horaria"],
        datos["Clase_Cabina"],
        datos["Tipo_Pasajero"],
    )
    assert isinstance(resultado, bool)

def test_origen_igual_destino_es_invalido():
    """Una reserva con mismo origen y destino debe rechazarse."""
    valido, motivo = validar_reserva(
        "Madrid", "Madrid", "Noche", "Ejecutiva", "Adulto"
    )
    assert valido is False
    assert "iguales" in motivo

def test_nino_en_ejecutiva_es_invalido():
    """Un nino en clase ejecutiva debe rechazarse."""
    valido, motivo = validar_reserva(
        "Quito", "Lima", "Manana", "Ejecutiva", "Nino"
    )
    assert valido is False

def test_reserva_valida_es_aceptada():
    """Una reserva correcta debe aceptarse."""
    valido, motivo = validar_reserva(
        "Quito", "Lima", "Madrugada", "Economica", "Adulto"
    )
    assert valido is True
    assert motivo == "OK"