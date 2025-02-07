import sqlite3

def connect_db():
    # Use a dedicated database file for inventory data
    conn = sqlite3.connect('inventory_shop.db')
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create an Inventory table that tracks flavor stock levels
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventory (
            id INTEGER PRIMARY KEY,
            flavor TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    
    # Optionally, you can include an Ingredients table if needed
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    
    # Optionally, include an Allergens table if relevant for the service
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Allergens (
            id INTEGER PRIMARY KEY,
            allergen TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def update_inventory(flavor, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    # Check if the flavor exists in the inventory
    cursor.execute("SELECT id FROM Inventory WHERE flavor = ?", (flavor,))
    result = cursor.fetchone()
    if result:
        cursor.execute("UPDATE Inventory SET quantity = ? WHERE flavor = ?", (quantity, flavor))
    else:
        cursor.execute("INSERT INTO Inventory (flavor, quantity) VALUES (?, ?)", (flavor, quantity))
    conn.commit()
    conn.close()

def get_inventory():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Inventory")
    inventory = cursor.fetchall()
    conn.close()
    return inventory
