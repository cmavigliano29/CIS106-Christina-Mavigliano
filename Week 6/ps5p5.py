sumdiscounts = 0

r = input("Would you like to run the program? ('Yes' to proceed) ")
while(r=="Yes"):
  qty = float(input("Enter quantity of item "))
  price = float(input("Enter price of item "))
  extprice = qty * price
  if extprice > 10000.00:
    discount = 0.25
  else:
    discount = 0.10
  discountamount = discount * extprice
  total = extprice - discountamount
  print("Extended price: " , extprice)
  print("Discount amount " , discountamount)
  print("Total: " , total)
  sumdiscounts = sumdiscounts + discountamount
  r = input("Would you like to run the program again? ('Yes' to proceed) ")

print("Sum of all discounts: " , sumdiscounts)