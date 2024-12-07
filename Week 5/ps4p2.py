#input phase
part = input("Enter part number ")
qty = float(input("Enter quantity of part "))

#process phase
if part == "10" or part == "55":
  unitcost = 1.00
elif part == "99":
  unitcost = 2.00
elif part == "80" or part == "70":
  unitcost = 3.00
else:
    unitcost = 5.00
total = qty * unitcost

#output phase
print("Part number: ", part)
print("Unit cost: ", unitcost)
print("Total: " , total)