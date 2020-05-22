import psycopg2

DB_NAME = "observ_db"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

try: 
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

    print("Database connect successfully...")

except:
    print("Database not connected")

cur = conn.cursor()

