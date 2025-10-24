from faker import Faker
import pandas as pd, numpy as np
from datetime import datetime, timedelta
fake = Faker('es_ES')

orders = []
for _ in range(5000):
    orders.append({
        "order_id": fake.uuid4(),
        "customer_id": np.random.randint(1000, 2000),
        "order_datetime": fake.date_time_between(start_date='-180d', end_date='now'),
        "order_total": round(np.random.uniform(25, 250), 2),
        "payment_status": np.random.choice(["Aprobado", "Pendiente", "Rechazado"], p=[0.85, 0.10, 0.05])
    })
df_orders = pd.DataFrame(orders)
df_orders.to_csv("bronze/orders.csv", index=False)
