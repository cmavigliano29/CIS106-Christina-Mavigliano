#input phase
item = input("Enter item name ")
qty = float(input("Enter quantity of item "))

#process phase
if item == "A":
    unitprice = 10.00
else:
    unitprice = 20.00

extendedprice = qty * unitprice

#output phase
print("Item:" , item )
print("Unit price:" , unitprice)
print("Extended price:" , extendedprice)