import sqlite3
from collections import defaultdict
def setup():
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect("boards.db")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Create a table with a date column and a board column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boards (
            id INTEGER PRIMARY KEY,
            json_content TEXT,
            date TEXT
        )
    ''')
    return connection, cursor

def cleanup(connection):
    # Commit the changes and close the connection
    connection.commit()
    connection.close()


def insert(date, json_data):
    connection, cursor = setup()
    cursor.execute("""
    SELECT COUNT(*) FROM Boards WHERE date = ?;
    """, (date,))

    # If count is not 0, the record exists, so we don't insert it and return failure
    if cursor.fetchone()[0] != 0:
        cleanup(connection)
        return False
    
    cursor.execute('INSERT INTO boards (json_content, date) VALUES (?, ?)', (json_data, date))
    cleanup(connection)
    return True

def get(date):
    connection, cursor = setup()
    cursor.execute("SELECT * FROM boards WHERE date = ?", (date,))
    results = cursor.fetchall()
    cleanup(connection)

    # no results or too many results; smth is wrong so dont give back anything
    if len(results) != 1:
        return None
    return results

if __name__ == "__main__":

    board = get("2025-01-02")
    print(board)


