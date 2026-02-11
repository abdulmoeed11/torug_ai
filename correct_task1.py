def calculate_average_order_value(orders):
    """
    Calculates the average order value from a list of orders, ignoring cancelled ones.
    
    Args:
        orders (list): A list of dictionaries, each containing 'status' and 'amount'.
        
    Returns:
        float: The average value of non-cancelled orders. Returns 0.0 if there are no valid orders.
    """
    if not orders:
        return 0.0
    
    total = 0
    valid_order_count = 0

    for order in orders:
        # Check if keys exist to avoid KeyError
        if "status" not in order or "amount" not in order:
            continue
            
        if order["status"] != "cancelled":
            # Ensure amount is a number
            if isinstance(order["amount"], (int, float)):
                total += order["amount"]
                valid_order_count += 1

    if valid_order_count == 0:
        return 0.0

    return total / valid_order_count
