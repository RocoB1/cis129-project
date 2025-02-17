# This project collects user inputs and makes calculations to determine what their receipt should look like
# Roco Bellavia
print('********************************')
print('Welcome To SweetJava')
#Collect user input and convert from string to integer
num_coffee = int(input("How many cups of coffee would you like? "))
num_muffin = int(input("How many muffins would you like? "))
num_donuts = int(input("How many donuts would you like? "))
num_tea = int(input("How many tea would you like? "))
'''
num_coffee * $5 + num_muffins * $4 * 0.06
'''
#Perform calculations to show on receipt
subtotal = (num_coffee * 5) + (num_muffin * 4) + (num_donuts * 2) + (num_tea * 1)
tax = subtotal * 0.06
total = subtotal + tax

# Print the receipt
print("********************************")
print("SweetJava Receipt")
print("--------------------------------")
print("Number of coffees bought?")
print(num_coffee)
print("Number of muffins bought?")
print(num_muffin)
print("Number of donuts bought?")
print(num_donuts)
print("Number of tea bought?")
print(num_tea)
print("--------------------------------")
print(num_coffee, "Coffee at $5 each: $" + str(num_coffee * 5))
print(num_muffin, "Muffins at $4 each: $" + str(num_muffin * 4))
print(num_donuts, "Donuts at $2 each: $" + str(num_donuts * 2))
print(num_tea, "Tea at $1 each: $" + str(num_tea * 1))
print("Tax: $" + str(tax))
print("--------------------------------")
print("Total: $" + str(total))
print("********************************")
print('Thank You for choosing SweetJava hope to see you again!')


