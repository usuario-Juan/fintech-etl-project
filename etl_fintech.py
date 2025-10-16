import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

# === CONFIGURATION ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'fintech_sales', 'sales_q1.csv')
EXCEL_PATH = os.path.join(BASE_DIR, 'fintech_sales', 'clients.xlsx')

DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'fintech_db',
    'user': 'postgres',
    'password': os.getenv('DB_PASSWORD') 
}

# === 1. Verify files ===
print("🔍 Verifying files...")
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Not found: {CSV_PATH}")
if not os.path.exists(EXCEL_PATH):
    raise FileNotFoundError(f"Not found: {EXCEL_PATH}")

print("Files found")

# === 2. Load data ===
print("📥 Loading data...")
try:
    sales = pd.read_csv(CSV_PATH, parse_dates=['date'])
    clients = pd.read_excel(EXCEL_PATH, sheet_name='data')
    print(f"Sales loaded: {len(sales)} records")
    print(f"Clients loaded: {len(clients)} records")
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

# === 3. Cleanse and transform ===
print("🧹 Cleaning data...")
# Convert 'amount' to numeric and drop invalid rows
sales['amount'] = pd.to_numeric(sales['amount'], errors='coerce')
sales.dropna(subset=['amount'], inplace=True)  # ← was 'clients', now 'sales'

# Merge datasets
datos = pd.merge(sales, clients, on='client_id', how='left')

# Extract month from 'date' column (not 'data')
datos['month'] = datos['date'].dt.month

print(f"Clean data: {len(datos)} records")

# === 4. Connect and create table ===
print("Connecting to PostgreSQL...")
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    print("Connection successful")

    # Create table (use consistent English name)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales_fintech (
            sales_id INT,
            date DATE,
            product VARCHAR(100),
            amount NUMERIC,
            client_id VARCHAR(10),
            name VARCHAR(100),
            region VARCHAR(50),
            month INT
        );
    """)
    print("Table 'sales_fintech' created (if it did not exist)")

    # Insert data into the CORRECT table name
    for _, row in datos.iterrows():
        cur.execute(
            "INSERT INTO sales_fintech VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row)
        )
    conn.commit()
    print(f"Inserted {len(datos)} records")

    cur.close()
    conn.close()
    print("Connection closed")

except Exception as e:
    print(f"Database error: {e}")
    exit(1)

# === 5. Generate report ===
print("\n=== AUTOMATED SALES REPORT ===")
print(f"Total sales: {len(datos)}")
print(f"Total revenue: {datos['amount'].sum():,.2f} RUB")  # ← 'amount', not 'monto'
print("\nRevenue by region:")
print(datos.groupby('region')['amount'].sum().round(2))   # ← 'amount'
print("\nTop-selling product:")
print(datos['product'].mode()[0])  # ← 'product', no extra character