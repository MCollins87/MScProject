import os
import subprocess
import logging
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DB_CONFIG = {
    "host": os.getenv("PGHOST"),
    "port": os.getenv("PGPORT"),
    "dbname": os.getenv("PGDATABASE"),
    "user": os.getenv("PGUSER"),
    "password": os.getenv("PGPASSWORD"),
}

logging.basicConfig(
    filename=r"C:\IDR\logs\etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting master ETL process.")
logging.info("Running ARIA RT Referral ETL...")
try:
    subprocess.run(["python", "etl_load_ARIA_RT_Referral.py"], check=True)
    logging.info("ARIA RT Referral ETL completed.")
except subprocess.CalledProcessError as e:
    logging.error(f"ARIA RT Referral ETL failed: {e}")

logging.info("Running ARIA First Treatment ETL...")
try:
    subprocess.run(["python", "etl_load_ARIA_Treat.py"], check=True)
    logging.info("ARIA First Treatment ETL completed.")
except subprocess.CalledProcessError as e:
    logging.error(f"ARIA First Treatment ETL failed: {e}")

logging.info("Running ARIA CT ETL...")
try:
    subprocess.run(["python", "etl_load_ARIA_CT.py"], check=True)
    logging.info("ARIA CT ETL completed.")
except subprocess.CalledProcessError as e:
    logging.error(f"ARIA CT ETL failed: {e}")

logging.info("Running Intake ETL...")
try:
    subprocess.run(["python", "etl_load_intake.py"], check=True)
    logging.info("Intake ETL completed.")
except subprocess.CalledProcessError as e:
    logging.error(f"Intake ETL failed: {e}")

logging.info("Master ETL process completed successfully.")

def build_fact_table():
    logging.info("Starting fact table build process.")
    try:
        with open(r"C:\IDR\SQL\build_fact_table.sql", "r") as f:
            sql = f.read()

        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Fact table build completed.")
    except Exception as e:
        logging.error(f"Fact table build failed: {e}")
