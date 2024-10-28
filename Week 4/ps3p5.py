#input phase
lname = input("Enter last name ")
dependents = float(input("Enter number of dependents "))
gross = float(input("Enter gross income "))

#process phase
adjgross = gross - (dependents * 12000)

if adjgross > 50000.00:
  taxrate = 0.20
else:
  taxrate = 0.10

tax = adjgross * taxrate

if tax < 0:
  tax = 100.00

#output phase
print("Last name: " , lname)
print("Gross income: " , gross)
print("Number of dependents: " , dependents)
print("Adjusted gross income: " , adjgross)
print("Income tax: " , tax)