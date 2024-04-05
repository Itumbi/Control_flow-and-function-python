def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount=price * (discount / 100)
        final_price=price - discount_amount
        return final_price
    else:
        return price
    
# Prompting the user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculating the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount)

# Proving if a discount was applied
if final_price != original_price:
    print("Final price after discount: $", final_price)
else:
    print("No discount applied. Final price: $", final_price)