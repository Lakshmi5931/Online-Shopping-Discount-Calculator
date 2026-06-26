customer_name = input("Enter Customer Name: ")
product_price = float(input("Enter Product Price (₹): "))
if product_price >= 5000:
    discount = 20
elif product_price >= 3000:
    discount = 15
elif product_price >= 1000:
    discount = 10
else:
    discount = 5
discount_amount = (product_price * discount) / 100
final_amount = product_price - discount_amount
print("\n===== SHOPPING BILL =====")
print("Customer Name :", customer_name)
print("Product Price : ₹", product_price)
print("Discount      :", discount, "%")
print("Amount Saved  : ₹", discount_amount)
print("Final Amount  : ₹", final_amount)
print("--------------------------")