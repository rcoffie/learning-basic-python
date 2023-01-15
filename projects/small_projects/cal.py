''' The users inputs for the numbers and the operators '''
num1 = float(input('Enter your first number:'))
Operator = input('Enter Operator')
num2 = float(input('ENter your second number'))

''' if operator is (+ | - | * | /) then print out the number 1(+ | - | /)  number '''
if Operator == '+':
    print(num1 + num2)
elif Operator == '_':
    print(num1 - num2)
elif Operator == '/':
    print(num1 / num2)
elif Operator == '*':
    print(num1 * num2)

else:
    print('Not a Valid Operator')