## Proceso de extracción de datos (simulado)

Dado que el sistema se encuentra en desarrollo, los datos del análisis se **generarán mediante simulación controlada**, replicando condiciones reales de operación para un e-commerce de pastelería con CRM y marketing digital. La simulación producirá tablas coherentes entre sí (órdenes, ítems, clientes, campañas, eventos de CRM, navegación web, anuncios y pagos) con volúmenes y distribuciones plausibles, incluyendo estacionalidad (fechas clave) y diferencias de comportamiento entre clientes nuevos y recurrentes.

El flujo se organiza en tres fases:

1. **Generación sintética** con scripts en Python (`faker`, `numpy`, `pandas`) para crear entidades y eventos realistas (IDs, fechas, montos, categorías, estados).
2. **Almacenamiento estructurado** en un data lake local con capas:
   - **bronze**: datos crudos en CSV/JSON particionados por fecha/origen.
   - **silver**: datos limpios y tipados (Parquet), fechas normalizadas (UTC-4) y esquemas unificados.
   - **gold**: vistas analíticas (embudos, cohortes, RFM) y datasets de entrenamiento (features + target).
3. **Limpieza y transformación** para asegurar coherencia referencial (llaves primarias/foráneas), manejo de nulos, normalización de categorías y enriquecimiento con dimensiones (UTM, feriados, taxonomías).

**Ética y seguridad.** Al no usar datos reales, se elimina el riesgo sobre información personal. El proceso documenta prácticas de privacidad y seguridad para su futura aplicación en producción (credenciales en `.env`, permisos de solo lectura, rotación de claves).

**Evidencia reproducible (fragmento de ejemplo):**
```python
from faker import Faker
import pandas as pd, numpy as np
fake = Faker('es_ES')

orders = [{
    "order_id": fake.uuid4(),
    "customer_id": np.random.randint(1000, 2000),
    "order_datetime": fake.date_time_between(start_date='-180d', end_date='now'),
    "order_total": round(np.random.uniform(25, 250), 2),
    "payment_status": np.random.choice(["Aprobado","Pendiente","Rechazado"], p=[0.85,0.10,0.05])
} for _ in range(5000)]

pd.DataFrame(orders).to_csv("bronze/orders.csv", index=False)
