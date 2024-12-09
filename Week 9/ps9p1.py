def compForecast(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    forecastpercent = 0.10
  elif month == "Apr" or month == "May" or month == "Jun":
    forecastpercent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    forecastpercent = 0.20
  else:
    forecastpercent = 0.25

  forecast = sales * (1 + forecastpercent)
  return forecast

r = input("Would you like to predict next month's sales? (y/n) ")
while (r=="y"):
  lname  = input("Enter last name ")
  month = input("Enter month ")
  sales = float(input("Enter sales "))
  forecast = compForecast(month, sales)
  print("Next month's sales: ", forecast)
  r = input("Would you like to predict next month's sales? (y/n) ")