import sqlite3

# Function to connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('ice_cream_shop.db')
    return conn

# Function to initialize the database
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Creating tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Flavors (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        seasonal BOOLEAN NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Ingredients (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Allergens (
                        id INTEGER PRIMARY KEY,
                        allergen TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Cart (
                        id INTEGER PRIMARY KEY,
                        flavor_id INTEGER,
                        FOREIGN KEY (flavor_id) REFERENCES Flavors(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Suggestions (
                        id INTEGER PRIMARY KEY,
                        flavor_name TEXT NOT NULL,
                        comment TEXT)''')

    conn.commit()
    conn.close()

# Add a new flavor to the database
def add_flavor(name, seasonal):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Flavors (name, seasonal) VALUES (?, ?)", (name, seasonal))
    conn.commit()
    conn.close()

# Add a new ingredient
def add_ingredient(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Ingredients (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Add a new allergen
def add_allergen(allergen):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Allergens (allergen) VALUES (?)", (allergen,))
    conn.commit()
    conn.close()

# Add a suggestion
def add_suggestion(flavor_name, comment):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Suggestions (flavor_name, comment) VALUES (?, ?)", (flavor_name, comment))
    conn.commit()
    conn.close()

# Fetch all seasonal flavors
def get_seasonal_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flavors WHERE seasonal = 1")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

# Fetch all flavors
def get_all_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

# Fetch all ingredients
def get_all_ingredients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredients")
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

# Fetch allergens for ingredients
def get_allergens():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Allergens")
    allergens = cursor.fetchall()
    conn.close()
    return allergens

# Add a flavor to the cart
def add_to_cart(flavor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cart (flavor_id) VALUES (?)", (flavor_id,))
    conn.commit()
    conn.close()

# View all cart items
def view_cart():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Flavors.name FROM Flavors JOIN Cart ON Flavors.id = Cart.flavor_id")
    cart_items = cursor.fetchall()
    conn.close()
    return cart_items

"""from database import add_flavor

# Add seasonal flavor
add_flavor("Strawberry Cheesecake", True)  # Seasonal flavor
# Add a regular flavor
add_flavor("Vanilla", False)  # Not seasonal

from database import add_ingredient

# Add ingredients
add_ingredient("Milk")
add_ingredient("Sugar")
add_ingredient("Chocolate Chips")

from database import add_allergen

# Add allergens
add_allergen("Nuts")
add_allergen("Dairy")

from database import add_suggestion

# Add a flavor suggestion
add_suggestion("Chocolate Mint", "A chocolate mint flavor would be great for summer!")"""

