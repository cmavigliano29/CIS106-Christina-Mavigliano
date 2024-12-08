#before - initialize sums and set counts to 0
c = 0

#prompt user
r = input("Would you like to run the program? ('Yes' to proceed) ")
while(r=="Yes"):
  lname = input("Enter your last name ")
  exam1 = float(input("Enter exam 1 score "))
  exam2 = float(input("Enter exam 2 score "))
  avg = (exam1 + exam2) / 2
  print("Student: " , lname)
  print("Average: " , avg)
  c = c + 1
  r = input("Would you like to run the program again? ('Yes' to proceed) ")

#after
print("Number of students who entered data: " , c)