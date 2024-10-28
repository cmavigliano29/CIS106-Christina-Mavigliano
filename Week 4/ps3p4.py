#input phase
name = input("Enter name of appliance ")
cost = float(input("Cost of appliance "))

#process phase
if cost > 1000:
  warranty = 0.10 * cost
else:
  warranty = 0.05 * cost

total = cost + warranty

#output phase
print("Name of appliance: " , name)
print("Cost of appliance: " , cost)
print("Cost of warranty: " , warranty)
print("Total: " , total)