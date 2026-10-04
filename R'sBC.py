# Rubinosław's Basic Calculator

num_1 = float(input("Please insert the first number: "))
num_2 = float(input("Please insert the second number: "))

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Floor Division")

operation = input("Please choose an operation: ")

if operation == "1":
    print(num_1 + num_2)

elif operation == "2":
    print(num_1 - num_2)
    
elif operation == "3":
    print(num_1 * num_2)
    
elif operation == "4":
    if num_2 == 0:
        print("You cannot divide by zero!")
    else:
        print(num_1 / num_2)
        
elif operation == "5":
    print(num_1 ** num_2)
    
elif operation == "6":
    if num_2 == 0:
        print("You cannot divide by zero!")
    else:
        print(num_1 // num_2)
        
else:
    print("Invaild operation!")
