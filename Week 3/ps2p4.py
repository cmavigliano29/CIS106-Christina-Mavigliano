#input phase
make = input("Enter make of car")
model = input("Enter model of car")
msrp = float(input("Enter msrp of car"))
discount = float(input("Enter discount percentage"))

#process phase
amountoff = msrp * discount
discountedprice = msrp - amountoff

#output phase
print("Make of car: ", make)
print("Model of car: ", model)
print("MSRP of car: ", msrp)
print("Discount percentage: ", discount)
print("Amount off: ", amountoff)
print("Discounted price: ", discountedprice)