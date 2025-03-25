def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# call the function in a final price variable
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {final_price:.2f}")
