"""
UIDE - Diseño de Pruebas, Control de Calidad y Mantenimiento
Generador de casos de prueba por combinación de pares (pairwise testing).
Sistema de Reserva de Vuelos - Diseño de Experimentos (DOE).
"""
from allpairspy import AllPairs

# Definición de factores y sus niveles
factores = {
    "Ciudad_Origen": ["Quito", "Guayaquil", "Cuenca", "Madrid", "Bogota"],
    "Ciudad_Destino": ["Lima", "Madrid", "Miami", "Panama", "Buenos_Aires"],
    "Franja_Horaria": ["Madrugada", "Manana", "Mediodia", "Tarde", "Noche"],
    "Clase_Cabina": ["Economica", "Ejecutiva"],
    "Tipo_Pasajero": ["Adulto", "Nino", "Tercera_Edad"],
}

nombres = list(factores.keys())
valores = list(factores.values())

print("=" * 80)
print("CASOS DE PRUEBA - COMBINACION POR PARES (PAIRWISE)")
print("Sistema de Reserva de Vuelos")
print("=" * 80)

# Encabezado
encabezado = "Caso | " + " | ".join(nombres)
print(encabezado)
print("-" * 80)

# Generación de casos pairwise
total = 0
for i, caso in enumerate(AllPairs(valores), start=1):
    fila = f"CP-{i:02d} | " + " | ".join(str(v) for v in caso)
    print(fila)
    total += 1

print("-" * 80)
print(f"Total de casos generados con pairwise: {total}")
print(f"Total de combinaciones exhaustivas: {5*5*5*2*3} = 750")
print(f"Reduccion: {round((1 - total/750) * 100, 1)}% menos casos de prueba")