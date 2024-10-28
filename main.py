# main.py

from order import place_order
from invoice import generate_invoice

def main():
    """Main function to run the restaurant management system."""
    while True:
        print("\n1. Place Order")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            order, total_cost = place_order()
            if order:
                generate_invoice(order, total_cost)
        elif choice == '2':
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
