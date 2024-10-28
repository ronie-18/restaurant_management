# order.py

from menu import menu, inventory

def place_order():
    """Allows the customer to place an order and returns the order summary."""
    order = {}
    total_cost = 0

    print("\n--- Place Your Order ---")
    n = int(input("How many items would you like to order? "))

    for _ in range(n):
        item = input("Enter item name: ").strip()
        quantity = int(input("Enter quantity: "))

        # Check if item exists in the menu and stock is sufficient
        if item in menu:
            if inventory[item] >= quantity:
                order[item] = quantity
                inventory[item] -= quantity  # Update stock
                total_cost += menu[item] * quantity
            else:
                print(f"Sorry, only {inventory[item]} {item}(s) available.")
        else:
            print(f"{item} is not on the menu.")

    if order:
        print(f"\nOrder placed successfully! Total: ${total_cost}")
        return order, total_cost
    else:
        print("No valid items in the order.")
        return None, 0
