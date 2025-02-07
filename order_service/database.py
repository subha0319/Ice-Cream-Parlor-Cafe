import sqlite3

def connect_db():
    # Use a dedicated database file for order data
    conn = sqlite3.connect('order_shop.db')
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create an Orders table to track customer orders.
    # Note: In a microservices setup, cross-service foreign keys are avoided.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY,
            flavor_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def create_order(flavor_id, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Orders (flavor_id, quantity) VALUES (?, ?)", (flavor_id, quantity))
    conn.commit()
    conn.close()

def get_orders():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    conn.close()
    return orders
