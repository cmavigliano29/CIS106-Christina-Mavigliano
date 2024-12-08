file = open("myfile.txt", "r")

bonustotal = 0.00

lname = str(f.readline().rstrip('\n'))

while item !="":
  salary = float(f.readline())
  if salary >=100000.00:
    bonusrate = 0.20
  elif salary >=50000.00:
    bonusrate  = 0.15
  else:
    bonusrate = 0.10
  bonus = salary * bonusrate
  bonustotal = bonustotal + bonus
  print("Employee last name:", lname)
  print("Salary:", salary)
  print("Bonus:", bonus)

print("Sum of bonuses:   ", bonustotal)