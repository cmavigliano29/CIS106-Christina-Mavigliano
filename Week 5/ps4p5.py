#input phase
lname = input("Enter employee last name ")
salary = float(input("Enter salary "))
level = float(input("Enter employee level "))

#process phase
if level >= 10:
  rate = 0.25
elif level >= 5:
  rate = 0.20
else:
  rate = 0.10
bonus = salary * rate

#output phase
print("Employee last name: " , lname)
print("Bonus: " , bonus)