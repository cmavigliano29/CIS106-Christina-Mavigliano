def CompMPG(miles, gallons):
  mpg = miles / gallons
  return mpg

c = 0
r = input ("Do you want to compute MPG? (y/n) ")
while r=="y":
  city = input("Enter city name ")
  miles = float(input("Enter miles driven "))
  gallons = float(input("Enter gallons used "))
  mpg = CompMPG(miles, gallons)
  print("City: ", city)
  print("Miles: ", miles)
  print("Miles per gallon: ", mpg)
  c = c + 1
  r = input ("Do you want to compute MPG? (y/n) ")

print("Total number of trips: ", c)