def CompExtPrice(qty, price):
  extprice = qty * unitprice

  if extprice > 10000:
    discamt = extprice * 0.10
  else:
    discamt = 0.0

  return extprice

totalextprice = 0.0
r = input ("Do you want to compute extended price (y/n)? ")

while r == "y":
  qty = float(input("Enter quantity "))
  unitprice = float(input("Enter unit price: "))
  extprice = CompExtPrice(qty, unitprice)
  totalextprice = totalextprice + extprice
  print("Entended price: ", extprice)
  r = input("Do you want to compute extended price (y/n)? ")

print("Total extended price: $", totalextprice)