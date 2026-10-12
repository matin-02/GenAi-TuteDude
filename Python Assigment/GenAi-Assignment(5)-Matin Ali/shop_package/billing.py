# created a billing.py file with calculate_total(prices) and apply_tax(amount) function 

def calculated_total(prices):
    # returning total bill
    return sum(prices)

def apply_tax(amount):
    # adding the 5% tax
    return amount + (amount * 5 / 100)