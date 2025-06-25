import pandas as pd
import numpy as np
import random
import sqlite3

# Parámetros
n = 2000
paises = ['México', 'Canadá', 'Brasil', 'Alemania', 'EEUU', 'España']
habitaciones = ['económica', 'estándar', 'lujo']
estados = ['completada', 'cancelada', 'confirmada']

df_simulado = pd.DataFrame({
    'id_reserva': range(1001, 1001 + n),
    'fecha_reserva': pd.to_datetime(np.random.choice(pd.date_range('2024-01-01', '2025-06-25'), size=n)),
    'id_cliente': ['C' + str(i).zfill(4) for i in range(1, n + 1)],
    'pais_cliente': np.random.choice(paises, size=n, p=[0.25, 0.2, 0.15, 0.15, 0.15, 0.1]),
    'id_habitacion': ['H' + str(random.randint(100, 499)) for _ in range(n)],
    'tipo_habitacion': np.random.choice(habitaciones, size=n, p=[0.4, 0.4, 0.2]),
    'monto_reserva': np.round(np.random.normal(loc=700, scale=250, size=n), 2),
    'estado_reserva': np.random.choice(estados, size=n, p=[0.7, 0.2, 0.1])
})

df_simulado['fecha_checkin'] = df_simulado['fecha_reserva'] + pd.to_timedelta(np.random.randint(1, 30, size=n), unit='D')
df_simulado['fecha_checkout'] = df_simulado['fecha_checkin'] + pd.to_timedelta(np.random.randint(1, 8, size=n), unit='D')

df_simulado['monto_reserva'] = df_simulado['monto_reserva'].apply(lambda x: x if x > 0 else abs(x) + 100)


conn = sqlite3.connect("reservas_simuladas.db")
df_simulado.to_sql("reservas", conn, if_exists="replace", index=False)
conn.close()
