from main import generate_invoice

# Dummy data for testing purposes
order = [
    {"item": "burger", "quantity": 2, "price_each": 5.00},
    {"item": "coke", "quantity": 3, "price_each": 2.00}
]
total_cost = 16.00

if __name__ == "__main__":
    generate_invoice(order, total_cost)
