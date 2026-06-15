# Aprendizaje Autónomo 2 - Técnicas Avanzadas de Testing de Software

UIDE - Sistemas de la Información
Asignatura: Diseño de Pruebas, Control de Calidad y Mantenimiento  
Estudiante: Jorge Pérez Rodríguez  

## Descripción

Este proyecto aplica tres técnicas de testing de software en Python:
combinación por pares (pairwise), análisis de cobertura de código y
análisis estático. El proyecto está desarrollado y probado en un entorno
GitHub Codespaces con Python 3.12.

## Estructura del proyecto

- `parte1_doe/` — Diseño de Experimentos y pruebas pairwise.
- `parte2_seccion1_cobertura/` — Algoritmo de búsqueda binaria y análisis de cobertura.
- `parte2_seccion2_estatico/` — Código con anomalías para análisis estático.
- `requirements.txt` — Dependencias del proyecto.

## Instalación

Crear el entorno virtual e instalar las dependencias:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

### Parte 1 — Pairwise testing

Generar los casos de prueba combinatorios:
```
python parte1_doe/pairwise_generator.py
```

Ejecutar las pruebas sobre los casos generados:
```
pytest parte1_doe/test_pairwise.py -v
```

### Parte 2 — Sección 1: Cobertura de código

Cobertura del conjunto inicial:
```
cd parte2_seccion1_cobertura
pytest test_inicial.py --cov=binary_search --cov-branch --cov-report=term-missing
```

Cobertura del conjunto mejorado (con reporte HTML):
```
pytest test_mejorado.py --cov=binary_search --cov-branch --cov-report=html
```

### Parte 2 — Sección 2: Análisis estático

```
pylint parte2_seccion2_estatico/binary_search_anomalias.py
flake8 parte2_seccion2_estatico/binary_search_anomalias.py
```

## Herramientas utilizadas

- allpairspy — generación de casos pairwise.
- pytest y pytest-cov (coverage.py) — pruebas unitarias y cobertura.
- pylint y flake8 — análisis estático del código.
