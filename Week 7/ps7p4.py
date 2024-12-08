file = open("myfile.txt", "r")

c = 0.0
tot_ep = 0.0

item = str(f.readline().rstrip('\n'))

while item !="":
  qty = float(f.readline())
  price = float(f.readline())
  ep = qty * price
  tot_ep = tot_ep + ep
  c = c + 1
  print("Item:           ", item)
  print("Quantity:       ", qty)
  print("Price:          ", price)
  print("Extended Price: ", ep)
  item = str(f.readline().rstrip('\n'))

print("Total Extended Prices:   ", tot_ep)
print("Number of Orders:        ", c)
avg = tot_ep / c
print("Average Order:           ", avg)