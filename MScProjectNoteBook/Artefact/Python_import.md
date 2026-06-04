Python script to load csv into PostgreSQL

# Import Dependencies

``` Python
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
```

## Load environment variables
Keeping with the 12 Factor App, no credentials should be hard coded into the script
``` Python
load_dotenc()
DB_CONFIG = {
	"host": os.getenv("PGHOST"),
	"port": os.getenv("PGPORT"),
	"dbname": os.getenv("PGDATABASE"),
	"user": os.getenv("PGUSER"),
	"password": os.getenv("PGPASSWORD"),
}

DATA_PATH = os.getenv("INTAKE_FILE_PATH", r"C:\IDR\oncology_intake_latest.csv")
```

## Some Helper Functions

``` Python
def clean_columns(df)
```