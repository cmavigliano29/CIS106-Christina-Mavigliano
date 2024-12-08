c = 0
total = 0

r = input("Would you like to run the program? ('Yes' to proceed) ")
while(r=="Yes"):
  lname = input("Enter last name ")
  hoursworked = float(input("Enter hours worked "))
  rate = float(input("Enter rate of pay "))
  grosspay = hoursworked * rate
  if(hoursworked > 40):
    grosspay = grosspay + (hoursworked - 40) * (rate / 2)
  print("Last name: " , lname)
  print("Gross pay: " , grosspay)
  c = c + 1
  total = total + grosspay
  r = input("Would you like to run the program again? ('Yes' to proceed) ")
avg = total / c

print("Sum of gross pays: " , total)
print("Number of employees: " , c)
print("Total of gross pays: " , avg)