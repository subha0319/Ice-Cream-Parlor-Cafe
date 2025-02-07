import sqlite3

def connect_db():
    # Using a dedicated database file for the flavor service
    conn = sqlite3.connect('flavor_shop.db')
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create the Flavors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Flavors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            seasonal BOOLEAN NOT NULL
        )
    ''')
    
    # Create the Suggestions table (for customer suggestions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Suggestions (
            id INTEGER PRIMARY KEY,
            flavor_name TEXT NOT NULL,
            comment TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def add_flavor(name, seasonal):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Flavors (name, seasonal) VALUES (?, ?)", (name, seasonal))
    conn.commit()
    conn.close()

def get_all_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def get_seasonal_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flavors WHERE seasonal = 1")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def add_suggestion(flavor_name, comment):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Suggestions (flavor_name, comment) VALUES (?, ?)", (flavor_name, comment))
    conn.commit()
    conn.close()
