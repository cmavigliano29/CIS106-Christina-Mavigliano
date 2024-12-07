#input phase
qtytickets = float(input("Enter quantity of tickets" ))

#process phase
if qtytickets >= 25:
  price = 50.00
elif qtytickets >= 10:
  price = 60.00
elif qtytickets >= 5:
  price = 70.00
else
  price = 75.00
total = qtytickets * price

#output phase
print("Number of tickets: " , qtytickets)
print("Price per ticket: " , price)
print("Total cost: " , total)