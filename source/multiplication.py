num1 = input("Enter two number: ")
num2 = num1.split(" ")
x1 = int(num2[0])
x2 = int(num2[1])


def multiply(x, y):
    output = x*y
    return output


print(multiply(x1, x2))
