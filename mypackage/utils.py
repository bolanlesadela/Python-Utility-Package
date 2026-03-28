def greet(name):
    return f"Hello, {name}! Welcome to MyPackage."

def calculate_total(items):
    """
    Takes a list of dicts with 'price' and 'qty' keys.
    Returns the total price.
    """
    return sum(item['price'] * item['qty'] for item in items)

def format_naira(amount):
    return f"NGN {amount:,.2f}"