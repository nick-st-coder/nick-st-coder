import psycopg2

DB_NAME = "enter-db-name-here"
DB_USER = "postgres"
DB_PASSWORD = "enter-db-password-here"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Succesful connection to PostgreSQL!")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM...;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)    