import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            rating TEXT,
            review TEXT,
            price TEXT,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new restaurant to the database
def add_restaurant(name, rating, review, price, location):
    name = input("Enter the name of the new restaurant: ")
    rating = input("Enter the rating of the restaurant: ")
    review = input("Enter a review for the restaurant: ")
    price = input("Enter the price range of the restaurant: ")
    location = input("Enter the location of the restaurant: ")

    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO restaurants (name, rating, review, price, location)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, rating, review, price, location))
    conn.commit()
    conn.close()

# Call initialize_database function
initialize_database()

# Example usage:
# Add some restaurants
add_restaurant("Stackd", "4.5/5", "I love the build your own burgers!", "$$", "Corner of Forbes & Oakland")
add_restaurant("Mount Everest Sushi", "5/5", "Best sushi in oakland YUM", "$$", "Oakland")

# # Function to remove a restaurant from the database by name
# def remove_restaurant_by_name(name):
#     conn = sqlite3.connect('restaurants.db')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM restaurants WHERE name = ?', (name,))
#     conn.commit()
#     conn.close()

# # # Example usage:
# remove_restaurant_by_name("Stackd")
# remove_restaurant_by_name("Mount Everest Sushi")

# Retrieve and print all restaurants
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM restaurants')
restaurants = cursor.fetchall()
conn.close()

for restaurant in restaurants:
    print("Name:", restaurant[1])
    print("Rating:", restaurant[2])
    print("Review:", restaurant[3])
    print("Price Range:", restaurant[4])
    print("Location:", restaurant[5])
    print()

