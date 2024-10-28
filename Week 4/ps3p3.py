# input phase
qtybooks = float(input("Enter quantity of books "))
cost = float(input("Enter cost per book "))

# process phase
total = qtybooks * cost

if total > 50.00:
  shipping = 0.00
else:
  shipping = 25.00

# output phase
print("Total: " , total")
print("Shipping " , shipping)