# This project collects user inputs and makes calculations to determine what their receipt should look like
# Roco Bellavia
print('********************************')
print('Welcome To SweetJava')
#Collect user input and convert from string to integer
num_coffee = int(input("How many cups of coffee would you like? "))
num_muffin = int(input("How many muffins would you like? "))
'''
num_coffee * $5 + num_muffins * $4 * 0.06
'''
#Perform calculations to show on receipt
subtotal = (num_coffee * 5) + (num_muffin * 4)
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
print("--------------------------------")
print(num_coffee, "Coffee at $5 each: $" + str(num_coffee * 5))
print(num_muffin, "Muffins at $4 each: $" + str(num_muffin * 4))
print("Tax: $" + str(tax))
print("--------------------------------")
print("Total: $" + str(total))
print("********************************")


