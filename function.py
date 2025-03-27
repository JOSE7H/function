# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function and get the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price or the original price
if final_price < original_price:
    print(f"The final price after applying a {discount_percentage}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")
