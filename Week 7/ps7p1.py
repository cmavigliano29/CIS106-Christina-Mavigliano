principle = float(input("Enter principle amount "))
rate = float(input("Enter interest rate as a decimal "))

total = 0

for x in range (1, 6, 1):
    annualinterest = principle * rate
    endingbal = principle + annualinterest
    total = total + annualinterest
    if x == 1:
        a1 = x
        b1 = principle
        c1 = endingbal
    if x == 2:
        a2 = x
        b2 = principle
        c2 = endingbal
    if x == 3:
        a3 = x
        b3 = principle
        c3 = endingbal
    if x == 4:
        a4 = x
        b4 = principle
        c4 = endingbal
    if x == 5:
        a5 = x
        b5 = principle
        c5 = endingbal
    principle = endingbal

print("Year          Beginning Balance          Ending Balance")
print(a1, "           $", b1, "                  $", c1)
print(a2, "           $", b2, "                  $", c2)
print(a3, "           $", b3, "                  $", c3)
print(a4, "           $", b4, "                  $", c4)
print(a5, "           $", b5, "                  $", c5)
print("Total interest earned: $", total)