# Análisis de Reservas por País – The Palace Company

Este proyecto realiza consultas SQL sobre una base de datos simulada de reservas hoteleras con el objetivo de analizar el comportamiento de los clientes por país.

## Archivos

- `reservas_simuladas.db`: Base de datos SQLite con datos ficticios de reservas.
- `Simulacion.py`: Script para generar y poblar la base de datos.
- `Consultas.ipynb`: Notebook con las consultas y visualización de resultados.

## Consultas realizadas

1. **Ingresos por país**  
   Suma total de reservas completadas por país de origen del cliente.

2. **Duración promedio de estancias**  
   Cálculo del número promedio de noches por país.

3. **Estacionalidad de reservas**  
   Distribución mensual de las reservas por país.

4. **Preferencias por tipo de habitación**  
   Cantidad de reservas por tipo de habitación segmentadas por país.

5. **Tasa de cancelación por país**  
   Porcentaje de reservas canceladas con respecto al total por país.

## Requisitos

- Python 3
- SQLite
- Jupyter Notebook
- Librerías: `pandas`, `matplotlib`, `ipython-sql`

---

