def CompTuition(hours, dcode):
  if dcode=="I":
    rate = 250.00
  else:
    rate = 550.00
  tuition = rate * hours
  return tuition

tuitionsum = 0
r = input ("Do you want to compute tuition? (y/n) ")
while r=="y":
  lname = input("Enter last name ")
  dcode = input("Enter district code ")
  hours = float(input("Enter number of credit hours "))
  tuition = CompTuition(hours, dcode)
  tuitionsum = tuitionsum + tuition
  print("Name: ", lname)
  print("Tuition: ", tuition)
  r = input ("Do you want to compute tuition? (y/n) ")

print("Total of all tuition: ", tuitionsum)