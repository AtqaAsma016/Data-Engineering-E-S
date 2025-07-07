#Basic Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print(f"Result: {num1 + num2}")
elif operation == '-':
    print(f"Result: {num1 - num2}")
elif operation == '*':
    print(f"Result: {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation!")



#Odd and Even Checker
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")


#Multiplication Table 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Reverse a string
text = input("Enter a string: ")
print(f"Reversed: {text[::-1]}")    


#Sum of Natural Numbers
n = int(input("Enter a number: "))
print(f"Sum of first {n} natural numbers: {n * (n + 1) // 2}")

#String Slicing
text = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
print(f"Sliced string: {text[start:end]}")

#Print Every Second Character
text = input("Enter a string: ")
print(f"Every second character: {text[::2]}")

#Fctorial using Loop
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")




