stocks = {"AAPL": 180, "TSLA": 250, "GOOGL": 500, "MSFT": 900, "AMZN": 100}
print("AVAILABLE STOCKS  AND THERIR PRICES:")
for i in stocks:
   print(i,"-",stocks[i])
print("--------------------------------------------------")
name = input("Enter the stock name to calculate investment value: ").upper()
quantity = input("Enter the quantity: ")
if name not in stocks:
    print("Invalid stock name. Please choose from the listed stocks.")
elif not quantity.isdigit() or int(quantity) <= 0:
    print("Invalid quantity. Please enter a positive integer.")
else:
    quantity = int(quantity)
    result = stocks[name] * quantity
    print(f"Total investment value for {quantity} shares of {name}: ₹{result}")
