print("========================================TASK 1========================================")
print()
import Math_utils

print(f"Addition of two Numbers : {Math_utils.add(1,2)}")
print(f"Substraction Of two Numbers : {Math_utils.subtract(3,5)}")

from Math_utils import square

print(f"The Square Of The Number is : {square(5)}")

print()
print("========================================TASK 2========================================")
print()

from String_utils import *
text = "hello how are you"

print("Capitalized : " ,capitalize_word(text))
#print()

print("Reversed : " , reverse_string(text))
#print()

print("Word Count : ",word_count(text))

print()
print("========================================TASK 3========================================")
print()

# Task 3:- printing and Checking all the modules working properly or not
from shop_package.discount import *
from shop_package.billing import *

price = 1000
discount_price = apply_discount(price , 10)
flat_price = flat_discount(price)

print("Discounted Price : ", discount_price)
print("Flat Discount Price : ", flat_price)

prices = [100,200,300]
total = calculated_total(prices)
total_with_tax = apply_tax(total)

print("Total Bill : " ,total)
print("Total With Tax : ",total_with_tax)

print()
print("========================================TASK 4========================================")
print()

# Task 4 :- in main.py importing the discount as disc and billing import calculate_total
# and calling every function

# importing the Shop_packages.discount as disc

import shop_package.discount as disc
from shop_package.billing import calculated_total
import shop_package

# calling very Function
print("Discount Price : ", disc.apply_discount(1000, 10))


print("Flat Discount Price : ", disc.flat_discount(1000))

print("Total Bill : ", calculated_total([100,200,300]))
print("Total With Tax : ",shop_package.billing.apply_tax(600))






