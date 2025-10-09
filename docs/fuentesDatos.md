# 5. Fuentes de Datos

El proyecto **“Bake IT!”** se sustenta en la generación, procesamiento y análisis de **datos simulados** que representan el funcionamiento real de un sistema de comercio electrónico especializado en pastelería. Dado que el sistema se encuentra en etapa de desarrollo y validación, se optará por **simular los conjuntos de datos** para emular el comportamiento de los usuarios, las ventas, los productos y la gestión de inventarios, garantizando así un entorno controlado para la aplicación de técnicas de Big Data.

---

## 5.1 Descripción de las Bases de Datos Simuladas

Las bases de datos se diseñarán con una estructura coherente con la arquitectura del sistema **“Bake IT!”**, basada en **PostgreSQL** y alimentada mediante scripts o generadores automáticos. Los conjuntos principales incluirán:

- **Usuarios:** datos simulados de clientes, emprendedores y administradores, con atributos como edad, ubicación, historial de compras y nivel de satisfacción.  
- **Productos:** catálogo de pasteles y postres con variables ficticias (nombre, ingredientes, categoría, precio, tiempo de preparación, nivel de demanda).  
- **Ventas y pedidos:** registros de transacciones generadas de manera aleatoria, con fechas, montos, estados de entrega y formas de pago realistas.  
- **Inventarios:** movimientos simulados de insumos (harina, azúcar, frutas, coberturas, etc.) que reflejen la dinámica de reposición y consumo.  
- **Logs y auditorías:** simulación de registros de accesos, actividad de usuarios y errores del sistema para el análisis de rendimiento.  
- **Reseñas y calificaciones:** comentarios generados automáticamente con lenguaje natural básico, para incorporar análisis de sentimientos.

---

## 5.2 Volumen y Estructura de los Datos

El conjunto total de datos simulados estará compuesto por **al menos 30,000 registros distribuidos entre las tablas principales** (usuarios, ventas, productos e inventario).  
Los datos serán generados mediante técnicas de **simulación controlada**, utilizando herramientas como **Python (pandas, faker, numpy)** o **scripts SQL**, con una estructura **tabular y semiestructurada** (CSV y JSON).  

El diseño del dataset buscará reflejar comportamientos realistas, tales como **picos de demanda en fechas festivas**, **productos más vendidos por temporada** o **usuarios frecuentes con preferencias personalizadas**.

---

## 5.3 Plan de Generación de Datos Simulados

La adquisición de datos se realizará en tres fases planificadas:

1. **Fase 1 (Semanas 1–2):** definición del modelo de datos y atributos principales de cada entidad.  
2. **Fase 2 (Semanas 3–5):** generación de los registros simulados usando *faker* y carga en la base de datos.  
3. **Fase 3 (Semanas 6–8):** validación de coherencia, limpieza y preparación de los datasets para análisis exploratorio y visualización.  

Además, se contempla ampliar el dataset con **datos externos públicos** de consumo alimentario y tendencias gastronómicas para complementar el análisis predictivo.

---

## 5.4 Consideraciones Éticas y Legales

Al tratarse de **datos simulados**, no se maneja información personal real ni sensible.  
No obstante, se mantendrán los principios de **ética, seguridad y trazabilidad** propios de un sistema Big Data, asegurando que los métodos de generación y análisis sean reproducibles y transparentes.  
En caso de integrar fuentes públicas, se respetarán los **términos de uso y licencias abiertas** de los datasets.

---

## 5.5 Relación con las 5V del Big Data

- **Volumen:** más de 30,000 registros simulados, escalables en pruebas.  
- **Velocidad:** generación automatizada y procesamiento inmediato.  
- **Variedad:** datos estructurados (ventas, inventarios) y no estructurados (reseñas, logs).  
- **Veracidad:** validación estadística de la coherencia de los datos generados.  
- **Valor:** los datos simulados permitirán probar técnicas de análisis predictivo y visualizar escenarios reales de decisión empresarial.
