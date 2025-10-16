# 📊 Fintech Sales ETL Project

This project simulates a data engineering pipeline for a fictional fintech company.  
It extracts sales and customer data from multiple sources, cleans it, loads it into a data warehouse (PostgreSQL), and generates an automated report with key metrics.

---

## 🚀 Features

- ✅ **Extraction**: Reads data from CSV and Excel files.
- ✅ **Transformation**: Cleans data, converts data types, merges sources, and computes derived metrics.
- ✅ **Loading**: Inserts data into a PostgreSQL database with automatic table creation.
- ✅ **Automation**: Generates a summary report in the console (revenue by region, top-selling product, etc.).

---

## 🛠️ Technologies Used

- **Language**: Python 3.x  
- **Libraries**:
  - `pandas` – Data processing and analysis
  - `psycopg2-binary` – PostgreSQL database adapter
  - `openpyxl` – Excel (.xlsx) file support
- **Database**: PostgreSQL
- **Environment Management**: `python-dotenv` for secure environment variables

---

## 🔧 Prerequisites

- [PostgreSQL](https://www.postgresql.org/download/) installed and running
- A database named `fintech_db` created
- `postgres` user with a known password

---

## ⚙️ Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/usuario-Juan/fintech-etl-project.git
   cd fintech-etl-project