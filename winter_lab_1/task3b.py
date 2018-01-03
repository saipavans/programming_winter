discount = 40/100
book_price_orig = 24.95
discounted_price = book_price_orig * (1 - discount)
initial_shipping_price = 3
recurring_shipping_price = 0.75
number_of_copies = 60

print("Total price for 60 books: ", ((discounted_price * number_of_copies) + initial_shipping_price + (recurring_shipping_price * (number_of_copies-1))))