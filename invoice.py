# invoice.py

from prettytable import PrettyTable # type: ignore
from menu import menu  # Importing the menu to get prices

def generate_invoice(order, total_cost):
    """Prints the invoice for the given order with a neat table."""
    
    # Create a PrettyTable object with appropriate column headers
    table = PrettyTable()
    table.field_names = ["Item", "Quantity", "Price (each)", "Total"]

    # Populate the table with order details
    for item, quantity in order.items():
        price_each = menu[item]
        total_price = price_each * quantity
        table.add_row([item, quantity, f"${price_each:.2f}", f"${total_price:.2f}"])

    # Print the invoice with total amount
    print("\n--- Invoice ---")
    print(table)
    print(f"Total Amount: ${total_cost:.2f}")
