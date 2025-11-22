num = int(input("Enter a number to divide : "))

if num == 0:
    print("Error: Division by zero is not allowed.")    
else:
    divisor = int(input("Enter a number to divide by : "))
    result = num / divisor
    print(f"The result of {num} divided by {divisor} is: {result}") 