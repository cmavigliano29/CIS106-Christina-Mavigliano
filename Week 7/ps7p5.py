file = open("myfile.txt", "r")

totaltuition = 0.0
c = 0.0

lname = str(f.readline().rstrip('\n'))

while item !="":
  dcode = float(f.readline())
  credits = float(f.readline())

  if dcode == "I":
    costpercredit = 250.00
  else:
    costpercredit = 500.00
    
  tuition = costpercredit * credits
  c = c + 1
  totaltuition = totaltuition + tuition
  lname = str(f.readline().rstrip('\n'))

print("Total tuition owed:   ", totaltuition)
print("Number of Students:        ", c)