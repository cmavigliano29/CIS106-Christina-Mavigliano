def CompPayRate(jobcode):
  if jobcode=="L":
    payrate = 25.00
  elif jobcode=="A":
    payrate = 30.00
  else:
    payrate = 50.00
  return payrate

totalpay = 0
r = input ("Do you want to compute payrate and gross pay? (y/n) ")
while r=="y":
  lname = input("Enter last name ")
  jobcode = input("Enter job code ")
  hours = float(input("Enter hours worked "))
  payrate = CompPayRate(jobcode)
  grosspay = payrate * hours
  if hours > 40:
    grosspay = grosspay + (hours - 40) /2 * payrate
  totalpay = totalpay + grosspay
  print("Name: ", lname)
  print("Gross pay: ", grosspay)
  r = input ("Do you want to compute payrate and gross pay? (y/n) ")

print("Total of all gross pay: ", totalpay)