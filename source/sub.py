"""num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = float(num1) - float(num2)
print("sub of {0} and {1} is {2}".format(num1,num2,num3))"""


def subtraction(x, y):
    z = x - y
    return z


x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

result = subtraction(x, y)
print("Subtraction of two numbers : ", result)

