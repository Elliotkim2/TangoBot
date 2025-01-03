import sqlite3
from collections import defaultdict
def setup():
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect("boards.db")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Create a table with a date column and a board column
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Boards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        board TEXT NOT NULL,
        crosses TEXT NOT NULL,
        equals TEXT NOT NULL
    );
    """)
    return connection, cursor

def cleanup(connection):
    # Commit the changes and close the connection
    connection.commit()
    connection.close()

# date="2024-12-23"
# board="EEEEEEEMEEEESMSEMEESEMSSEEEEMEEEEEEE"
def stringtoarr(board):
    grid = [[None]*6 for i in range(6)]
    for i, _ in enumerate(board):
        grid[i//6][i%6] = board[i]
    return grid

def arrtostring(grid):
    board = ""
    for row in grid:
        for c in row:
            board+=c
    return board

def listtostring(pairs):
    string = ""
    for i,j in pairs:
        string+=(f'{i},{j};')
    if string:
        string=string[:-1]
    return string

def stringtolist(string):
    pairs = []
    temp = string.split(";")
    for pair in temp:
        a,b=pair.split(",")
        pairs.append((int(a),int(b)))
    return pairs

def listtoadjlist(pairs):
    adj = [[] for i in range(36)]
    for a,b in pairs:
        adj[a].append(b)
        adj[b].append(a)
    return adj

def insert(date, board, crosses, equals):
    connection, cursor = setup()
    cursor.execute("""
    SELECT COUNT(*) FROM Boards WHERE date = ?;
    """, (date,))

    # If count is not 0, the record exists, so we don't insert it and return failure
    if cursor.fetchone()[0] != 0:
        cleanup(connection)
        return False
    
    cursor.execute("""
    INSERT INTO Boards (date, board, crosses, equals)
    VALUES (?, ?, ?, ?);
    """, (date,board,crosses,equals))
    cleanup(connection)
    return True

def get(date):
    connection, cursor = setup()
    cursor.execute("""
    SELECT * FROM Boards 
    WHERE date = ?;
    """, (date,))
    results = cursor.fetchall()
    
    cleanup(connection)

    # no results or too many results; smth is wrong so dont give back anything
    if len(results) != 1:
        return None
    return results[0]

if __name__ == "__main__":
    pass
    # insert("2024-12-23", "EEEEEEEMEEEESMSEMEESEMSSEEEEMEEEEEEE")
    board = get("2024-12-23")
    print(board)
    for c in board[2]:
        print(f'"{c}",',end=" ")
    print()
    print()
    print(listtoadjlist(stringtolist(board[3])))
    print()
    print(listtoadjlist(stringtolist(board[4])))
    # print(stringtoarr("EEEEEEEMEEEESMSEMEESEMSSEEEEMEEEEEEE"))
    # print(arrtostring(stringtoarr("EEEEEEEMEEEESMSEMEESEMSSEEEEMEEEEEEE")))
