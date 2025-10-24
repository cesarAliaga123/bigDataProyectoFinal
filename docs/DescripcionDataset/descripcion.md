## Ecosistema de datos

El ecosistema de datos se compone de varias fuentes consolidadas en un **data lake**. La base transaccional del e-commerce (Laravel/MySQL) aporta órdenes, ítems, clientes y cupones; el CRM (por ejemplo, Mailchimp, Brevo o solución propia) aporta campañas y eventos de engagement; la analítica web (GA4 o Matomo) entrega sesiones y eventos de navegación con sus UTM; las plataformas publicitarias (Meta Ads y Google Ads) proveen gasto, impresiones y clics por campaña, conjunto y anuncio; el procesador de pagos (Stripe o Mercado Pago) entrega estados de pago y comisiones; y el módulo de catálogo/inventario agrega productos, categorías, costos y stock.

A modo de referencia, los conjuntos de datos pueden denominarse:  
`ecom_orders`, `ecom_order_items`, `ecom_customers`, `ecom_products`, `crm_campaigns`, `crm_events`, `web_analytics_sessions`, `web_analytics_events`, `ads_meta`, `ads_google`, `payments_transactions`.

El tamaño exacto dependerá del histórico disponible; como guía, es habitual superar holgadamente el umbral de **30 000 registros** al integrar navegación, campañas y transacciones. Los tipos de datos abarcan variables **numéricas** (precio, cantidad, costo, margen, ROAS, CTR, CPC), **categóricas** (canal, campaña, categoría de producto, método de pago, estado del pedido), **texto** (nombres de productos, términos de búsqueda, contenido UTM) y **marcas de tiempo** (sesión, pedido, envío de campaña, aprobación de pago). Las **variables objetivo** varían según el caso de uso: conversión binaria, ticket promedio, recompra, CLV continuo y demanda por SKU/semana.

### Diccionario de variables (extracto de ejemplo)

| Fuente                 | Nombre variable   | Descripción                           | Tipo de dato |
|-----------------------|-------------------|---------------------------------------|--------------|
| ecom_orders           | order_id          | Identificador de la orden             | Entero       |
| ecom_orders           | order_datetime    | Fecha y hora de compra                | Fecha/Hora   |
| ecom_orders           | order_total       | Monto total de la orden               | Numérico     |
| ecom_order_items      | sku               | Código del producto                   | Texto        |
| ecom_order_items      | qty               | Cantidad del ítem                     | Entero       |
| ecom_products         | category          | Categoría (torta, cupcake, etc.)      | Categórico   |
| crm_events            | event_type        | send, open, click, unsubscribe        | Categórico   |
| web_analytics_events  | medium            | Medio (organic, cpc, email)           | Categórico   |
| ads_meta              | spend             | Gasto publicitario                    | Numérico     |
| payments_transactions | fee               | Comisión del procesador               | Numérico     |
