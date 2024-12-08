def CompBatAvg(numHits, atBats):
  batAvg = numHits / atBats
  return batAvg

c = 0

r = input("Do you want to calculate batting average? (Y/N) ")
while r=="y":
  lname = input("Enter last name ")
  numHits = float(input("Enter number of hits "))
  atBats = float(input("Enter at bats "))
  batAvg = CompBatAvg(numHits, atBats)
  print("Last name: ", lname)
  print("Batting average: ", batAvg)
  c = c + 1
  r = input("Do you want to calculate batting average? (Y/N) ")

print("Total players entered: ", c)