print("How many pennies do you have: ")
pennies = int(input())
print("How many nickels do you have: ")
nickels = int(input())
print("How many dimes do you have: ")
dimes = int(input())
print("How many quarters do you have: ")
quarters = int(input())
print("How many half-dollars do you have: ")
halfdollars = int(input())
print("How many one dollar bills do you have: ")
dollarbills = int(input())
money_total= (pennies * 0.01)+(nickels * 0.05)+(dimes * 0.10)+(quarters * 0.25)+(halfdollars * 0.50)+(dollarbills * 1.00)
if(pennies < 2):
    print("You have" ,pennies, "penny.")
else:
    print("You have" ,pennies, "pennies.")
if(nickels < 2):
    print("You have" ,nickels, "nickle.")
else:
    print("You have" ,nickels, "nickles.")
if(dimes < 2):
    print("You have" ,dimes, "dime.")
else:
    print("You have" ,dimes, "dimes.")
if(quarters < 2):
    print("You have" ,quarters, "quarter.")
else:
    print("You have" ,quarters, "quarters.")
if(halfdollars < 2):
    print("You have" ,halfdollars, "half dollar.")
else:
    print("You have" ,halfdollars, "half dollars.")
if(dollarbills < 2):
    print("You have" ,dollarbills, "one dollar bill.")
else:
    print("You have" ,dollarbills, "one dollar bills.")
print("The value of your coins is ${}.".format(money_total))