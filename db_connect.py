import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_root_password",
    database="alx_book_store"
)

cursor = conn.cursor()

# Test connection by retrieving tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("Tables in database:")
for table in tables:
    print(table[0])

# Close connection
cursor.close()
conn.close()
