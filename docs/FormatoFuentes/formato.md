## Formatos y fuentes

Los formatos predominantes en la adquisición son **CSV/TSV** para extracciones rápidas y **JSON** para APIs, mientras que **Parquet** se adopta en las capas analíticas por su eficiencia columnar. El origen de los datos combina plataformas web (GA4/Matomo), publicitarias (Meta, Google Ads), de pagos (Stripe o Mercado Pago), el CRM seleccionado y la base institucional interna del e-commerce. 

Cuando corresponde, se transforman archivos **JSON** o **CSV** a **Parquet** y se unifican esquemas; además, se armonizan zonas horarias y se enriquecen dimensiones con taxonomías de campañas, categorías y feriados locales.
