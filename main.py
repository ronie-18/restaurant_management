# restaurant_management.py

from prettytable import PrettyTable # type: ignore

# Menu and inventory data
menu = {
    "burger": 79.00,
    "pizza": 89.00,
    "pasta": 60.00,
    "coke": 25.00,
    "salad": 45.00
}
inventory = {
    "burger": 100,
    "pizza": 50,
    "pasta": 70,
    "coke": 200,
    "salad": 150
}

# Function to display menu
def show_menu():
    print("\n------------------ -:Menu:- ------------------")
    for item, price in menu.items():
        print(f"{item.capitalize()} - ₹{price:.2f}")

# Function to place an order with option to order more
def place_order():
    """Allows the customer to place an order and returns the order summary."""
    order = []
    total_cost = 0

    while True:
        print("\n---------------- -:Place Your Order:- ----------------")
        n = int(input("How many items would you like to order? "))

        for _ in range(n):
            item = input("Enter item name: ").lower()

            # Check if the item exists in the menu
            if item in menu:
                quantity = int(input("Enter quantity: "))

                # Check if enough stock is available
                if inventory[item] >= quantity:
                    # Add item to order and update stock
                    order.append({
                        "item": item,
                        "quantity": quantity,
                        "price_each": menu[item]
                    })
                    inventory[item] -= quantity  # Deduct stock
                    total_cost += menu[item] * quantity  # Update total cost
                else:
                    print(f"Sorry, only {inventory[item]} {item}(s) available.")
            else:
                print(f"{item.capitalize()} is not on the menu.")

        more = input("Would you like to order anything else? (yes/no): ").strip().lower()
        if more == 'no':
            break

    if order:
        print(f"\nOrder placed successfully! Total: ₹{total_cost:.2f}")
        return order, total_cost
    else:
        print("No valid items in the order.")
        return None, 0

# Function to generate an invoice
def generate_invoice(order, total_cost):
    """Prints the invoice for the given order with a neat table."""
    
    # Create a PrettyTable object with appropriate column headers
    table = PrettyTable()
    table.field_names = ["Item", "Quantity", "Price (each)", "Total"]

    # Populate the table with order details
    for item in order:
        total_price = item["price_each"] * item["quantity"]
        table.add_row([item["item"].capitalize(), item["quantity"], f"₹{item['price_each']:.2f}", f"₹{total_price:.2f}"])

    # Print the invoice with total amount
    print("\n--------------------- -:Invoice:- ---------------------")
    print(table)
    print(f"Total Amount: ₹{total_cost:.2f}")

# Function to process payment
def process_payment(total_cost):
    """Handles the payment process for the customer."""
    print("\n----------------- -:Payment Section:- -----------------")
    print(f"Total Amount to Pay: ₹{total_cost:.2f}")

    while True:
        try:
            amount = float(input("Enter payment amount: ₹"))
            if amount < total_cost:
                print(f"Insufficient payment! You need ₹{total_cost - amount:.2f} more.")
            elif amount >= total_cost:
                change = amount - total_cost
                print(f"Payment successful! Change: ₹{change:.2f}")
                print("Thank you for your purchase. Enjoy your meal!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

# Main function to run the application
def main():
    while True:
        print("\n-------------------- -:Restaurant Management System:- --------------------")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_menu()
        elif choice == '2':
            order, total_cost = place_order()
            if order:
                generate_invoice(order, total_cost)
                while True:
                    proceed_payment = input("Would you like to proceed to payment? (yes/no): ").lower()
                    if proceed_payment == 'yes':
                        process_payment(total_cost)
                        break
                    elif proceed_payment == 'no':
                        print("Thank you! You can pay later. Please proceed to the cashier when ready.")
                        break
                    else:
                        print("Invalid input. Please type 'yes' or 'no'.")
        elif choice == '3':
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
