import sqlite3
import os

# Delete the database file if it exists
if os.path.exists('customers.db'):
    os.remove('customers.db')

# Create a connection to the database
conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

# Create a table for customers
cursor.execute('''
CREATE TABLE customer (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    sales_amount REAL NOT NULL
)
''')

# Customer data
customers = [
    (1, 'John Doe', 'john.doe@example.com', 1000.0),
    (2, 'Jane Smith', 'jane.smith@example.com', 2000.0),
    (3, 'Fon Due', 'fon.due@example.com', 3000.0)
]

# Insert customer data
cursor.executemany('INSERT INTO customer VALUES (?, ?, ?, ?)', customers)
conn.commit()

print("Database created and data inserted successfully")

# 1. Select all customers
cursor.execute('SELECT * FROM customer')
all_customers = cursor.fetchall()
print("\nAll cutomers")
print(all_customers)

# 2. Select customers with sales amount > 1000
cursor.execute('SELECT name, sales_amount FROM customer WHERE sales_amount > 1000')
high_sales_customers = cursor.fetchall()
print("\nCutomers with sales greater than 1000")
for name, sales in high_sales_customers:
    print(f"{name:<15} {sales}")

# 3. Ask user for minimum sales and select customers above that amount
min_sales = float(input("\nEnter the minimum sales: "))
cursor.execute('SELECT name, sales_amount FROM customer WHERE sales_amount > ?', (min_sales,))
filtered_customers = cursor.fetchall()
print(f"Cutomers with sales greater than {min_sales:>8}")
for name, sales in filtered_customers:
    print(f"{name:<15} {sales}")

# Close the connection
conn.close()
