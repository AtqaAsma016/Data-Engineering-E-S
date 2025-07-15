# import csv

# # Set file path in the main folder
# file_path = "E:/MyVSCodeFiles/Data Intern E&S/sales_data.csv"

# # Sample enhanced data
# data = [
#     ["product", "category", "region", "sales"],
#     ["Laptop", "Electronics", "East", 1200.0],
#     ["Phone", "Electronics", "West", 800.0],
#     ["Tablet", "Electronics", "South", 900.0],
#     ["TV", "Electronics", "East", 1500.0],
#     ["Fan", "Electronics", "North", 200.0],
#     ["Chair", "Furniture", "East", 300.0],
#     ["Table", "Furniture", "South", 450.0],
#     ["Desk", "Furniture", "West", 700.0],
#     ["Sofa", "Furniture", "North", 1100.0],
#     ["Bookshelf", "Furniture", "East", 550.0]
# ]

# # Write data to CSV
# with open(file_path, mode='w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

# print(f"✅ CSV file created successfully at: {file_path}")





import csv

# ---- Create customer.csv ----
customers = [
    {"customer_id": 1, "customer_name": "Alice"},
    {"customer_id": 2, "customer_name": "Bob"},
    {"customer_id": 3, "customer_name": "Charlie"},
]

with open("spark_jobs/customer.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "customer_name"])
    writer.writeheader()
    writer.writerows(customers)

# ---- Create transactions.csv ----
transactions = [
    {"transaction_id": 101, "customer_id": 1, "product": "TV", "category": "Electronics", "amount": 500, "date": "2024-06-01"},
    {"transaction_id": 102, "customer_id": 1, "product": "Phone", "category": "Electronics", "amount": 700, "date": "2024-06-10"},
    {"transaction_id": 103, "customer_id": 2, "product": "Shoes", "category": "Fashion", "amount": 120, "date": "2024-06-15"},
    {"transaction_id": 104, "customer_id": 3, "product": "Watch", "category": "Fashion", "amount": 150, "date": "2024-06-05"},
    {"transaction_id": 105, "customer_id": 3, "product": "Shirt", "category": "Fashion", "amount": 100, "date": "2024-06-20"},
]

with open("spark_jobs/transactions.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["transaction_id", "customer_id", "product", "category", "amount", "date"])
    writer.writeheader()
    writer.writerows(transactions)

print("CSV files generated successfully in 'spark_jobs' folder.")
