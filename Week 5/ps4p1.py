#input phase
qty = float(input("Enter quantity of widgets "))

#process phase
if qty > 10000:
  price = 10.00
if qty >= 5000:
  price = 20.00
else:
  price = 30.00
extendedprice = qty * price
taxamount = 0.07 * extendedprice
total = extendedprice + taxamount

#output phase
print("Extended price: " , extendedprice)
print("Tax amount: " , taxamount)
print("Total: " , total)