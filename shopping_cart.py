Item = input("What item would you like to buy?: ")
Price = float(input("What is the price?: "))
Quantity = int(input("How many would you like?: "))
Total = Price * Quantity
print(f"You have bought {Quantity} x {Item} ")
print(f"Your total is : Rs.{Total}")
