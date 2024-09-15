#input phase
stockticker = input("Enter stock ticker symbol")
numshare = float(input("Enter number of shares"))
costshare = float(input("Enter cost per share"))

#process phase
amountinvested = numshare * costshare

#output phase
print("Amount invested: ", amountinvested)
