def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent/100))
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

try:   
# Prompt user to enter original price
    price = float(input("Enter the original price: "))
# Prompt user to enter discount percentage
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after discount is: {final_price}")

except:
    print("Please enter numeric values for the price and discount percentage")
