# 📊 Proyecto ETL: Análisis de Ventas en Fintech

Este proyecto simula un flujo de **ingeniería de datos** para una empresa fintech ficticia.  
Extrae datos de ventas y clientes desde múltiples fuentes, los limpia, los carga en un almacén de datos (PostgreSQL) y genera un informe automatizado con métricas clave.

---

## 🚀 Funcionalidades

- ✅ **Extracción**: Lectura de datos desde CSV y Excel.
- ✅ **Transformación**: Limpieza, conversión de tipos, combinación de fuentes y cálculo de métricas derivadas.
- ✅ **Carga**: Inserción en base de datos PostgreSQL con creación automática de tabla.
- ✅ **Automatización**: Generación de informe resumen en consola (ingresos por región, producto más vendido, etc.).

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python 3.x
- **Librerías**:
  - `pandas` – Procesamiento y análisis de datos
  - `psycopg2-binary` – Conexión a PostgreSQL
  - `openpyxl` – Lectura de archivos Excel (.xlsx)
- **Base de datos**: PostgreSQL
- **Gestión de entorno**: `python-dotenv` para variables de entorno seguras

---

## 🔧 Requisitos previos

- [PostgreSQL](https://www.postgresql.org/download/) instalado y ejecutándose
- Base de datos llamada `fintech_db` creada por el usuario
- Usuario `postgres` con contraseña conocida por el usuario

> 💡 ¿No tienes PostgreSQL? [Guía rápida de instalación para Windows](https://www.postgresql.org/download/windows/)

---

## ⚙️ Configuración local

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/fintech-etl-proyecto.git
   cd fintech-etl-proyecto