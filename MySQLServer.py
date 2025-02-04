import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',  # Update if MySQL is hosted elsewhere
            user='root',       # Use your MySQL username
            password='Mushrum@0312'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL server")

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # SQL statement to create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit the transaction (though it's not needed for CREATE DATABASE)
            connection.commit()

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure that the connection is properly closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()