#input phase
qtyitem = float(input("Enter quantity of item"))

#process phase
if qtyitem >= 1000:
  unitprice = 3.00
else:
  unitprice = 5.00

extendedprice = qtyitem * unitprice
tax = 0.07 * extendedprice
total = extendedprice + tax

#output phase
print("Quantity of item:" , qtyitem)
print("Unit price:" , unitprice)
print("Extended price:" , extendedprice)
print("Tax:" , tax)
print("Total:" , total)