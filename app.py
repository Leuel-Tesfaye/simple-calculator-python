number1 = int(input('Enter first number :'))
number2 = int(input('Enter the second number: '))

operator = input('Enter operator :')

if operator == '+' :
    print(f"The sum of the two numbers is : {number1 + number2}")

elif operator == '-' :
    print(f"The subtraction of the two numbers is : {number1 - number2}")

elif operator == '*' :
    print(f"The multiple of the two numbers is : {number1 * number2}")

elif operator == '/' :
    print(f"The sum of the two numbers is : { abs(number1 / number2)}")
else :
    print("Invalid operator")
