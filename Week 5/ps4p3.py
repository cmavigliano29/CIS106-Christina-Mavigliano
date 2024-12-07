#input phase
principle = float(input("Enter principle amount "))
year = input("Enter year to maturity ")

#process phase
if principle > 100000.00 and year == "5":
  rate = 0.06
elif principle >= 50000.00 and year == "10":
  rate = 0.05
elif principle >= 50000.00 and year == "5":
  rate = 0.04
else:
  rate = 0.02
interestamount = principle * rate

#output phase
print("Principle: " , principle)
print("Interest rate: " , rate)
print("Interest amount for first year: " , interestamount)