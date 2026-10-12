#Task 3: Create A simple Package(Shop_package)

# created a discount.py file with apply_discount and flat_discount

def apply_discount(price, percent):
    discount = price * percent / 100
    # returning the discount price
    return price - discount

def flat_discount(price):
    # always substarcting 50 from price
    return price - 50
