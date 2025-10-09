## 5.3 Plan de Adquisición de Datos

El plan de adquisición de datos del proyecto **“Bake IT!”** se basa en la **simulación controlada de información** que representa el comportamiento real de un sistema de comercio electrónico de pastelería.  
Su objetivo es garantizar la disponibilidad de un conjunto de datos **realista, coherente y voluminoso** para aplicar técnicas de análisis y modelado Big Data dentro del entorno del sistema.

---

### **Objetivos del Plan**
- Generar un dataset de al menos **30,000 registros simulados** representando operaciones reales del sistema.  
- Reproducir de forma creíble el comportamiento de **usuarios, ventas, productos, inventarios y reseñas**.  
- Asegurar la **calidad, consistencia y completitud** de los datos antes del análisis.  
- Permitir su integración con herramientas de análisis y visualización (Python, Power BI, SQL dashboards).  

---

### **Metodología**
La generación y adquisición de datos se realizará mediante procesos automáticos y técnicas de simulación:

- **Python (Faker, Pandas, NumPy):** para crear registros con comportamientos realistas.  
- **Scripts SQL:** para poblar la base de datos PostgreSQL manteniendo integridad referencial.  
- **CSV y JSON:** para exportación y análisis exploratorio.  
- **Fuentes complementarias abiertas:** en caso de necesitar datos de referencia gastronómica o de consumo.  

---

### **Fases del Plan (6 Semanas Totales)**

| **Semana** | **Fase / Actividad Principal** | **Descripción / Resultado Esperado** |
|-------------|--------------------------------|--------------------------------------|
| **Semana 1** | **Diseño del modelo de datos** | Definición de entidades, relaciones y atributos clave del sistema. |
| **Semana 2** | **Configuración de entorno y scripts** | Implementación de estructura en PostgreSQL y preparación de scripts de simulación. |
| **Semana 3** | **Generación inicial de datos simulados** | Creación automática de registros con Faker y carga en la base de datos. |
| **Semana 4** | **Validación y limpieza de datos** | Detección de inconsistencias, eliminación de duplicados y normalización de datos. |
| **Semana 5** | **Integración y análisis exploratorio** | Exportación de datos a herramientas de análisis, obtención de primeras métricas. |
| **Semana 6** | **Evaluación y documentación final** | Revisión de la calidad, preparación de reportes y documentación del proceso. |

---

### **Consideraciones Éticas y de Calidad**
- Los datos son **simulados**, sin información personal real.  
- Se aplicarán **controles automáticos** de calidad para validar coherencia, formato y consistencia.  
- Todo el proceso será **documentado y reproducible**, asegurando trazabilidad y transparencia.  

---

### **Resumen del Cronograma**
📅 **Duración total:** 6 semanas  
🧱 **Fases principales:** diseño → simulación → validación → análisis → documentación  
📊 **Entregables:** dataset validado, reportes exploratorios y documentación técnica del proceso.
