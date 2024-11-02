from main import place_order, generate_invoice, process_payment

if __name__ == "__main__":
    order, total_cost = place_order()
    if order:
        generate_invoice(order, total_cost)
        process_payment(total_cost)
