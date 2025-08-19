def calculate_discount (price, discount_percent):
    if discount_percent >= 20: # apply discount only if 20% or more
       discount_amount = (discount_percent / 100) * price
       final_price = price - discount_amount
       return  final_price
    else:
         return price


price = float(input("Enter the original price here:"))
discount_percent = float(input("Enter the discount percentage:"))


# calculate and show result
final_price = calculate_discount(price, discount_percent)


if discount_percent >= 20: 
        print(f"Discount applied! final price:{ final_price}")
else:
        print(f"No discount applied. original price:{final_price}")