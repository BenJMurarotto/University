import csv
from datetime import datetime, timedelta
import random

# Define the number of stores and transactions per store
num_stores = 5
transactions_per_store = 500
total_transactions = num_stores * transactions_per_store

# Function to generate a sequential transaction ID
def generate_transaction_id(row_num):
    return f"TXN-{row_num:04}"

# Function to generate random product details
def generate_product():
    product_id = random.randint(1000, 2000)  # Allow product IDs to repeat within this range
    product_name = f"Product {product_id}"
    cost = round(random.uniform(5, 50), 2)
    price = round(cost * random.uniform(1.5, 3.0), 2)
    return product_id, product_name, cost, price

# Generate the data and save to CSV
with open('weekly_sales_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Transaction ID', 'Store Location', 'Date', 'Time', 'Customer ID', 'Product ID', 'Product Name', 'Quantity', 'Cost', 'Price'])
    
    row_num = 1
    # Choose a random start date within the range of 10 years (2015 to 2024)
    start_date = datetime(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 24))
    end_date = start_date + timedelta(days=6)  # End date is 6 days after the start date for a 7-day period
    
    for store in range(1, num_stores + 1):
        for _ in range(transactions_per_store):
            transaction_id = generate_transaction_id(row_num)
            store_location = f"Store {store}"
            date = start_date + timedelta(days=random.randint(0, 6))  # Random day within the 7-day period
            time = f"{random.randint(10, 23)}:{random.randint(0, 59)}"
            customer_id = random.randint(10000, 99999)  # Customer IDs can repeat
            product_id, product_name, cost, price = generate_product()
            quantity = random.randint(1, 10)
            writer.writerow([transaction_id, store_location, date.strftime('%Y-%m-%d'), time, customer_id, product_id, product_name, quantity, cost, price])
            
            row_num += 1


print(f"Data generated and saved to 'weekly_sales_data.csv'.")
