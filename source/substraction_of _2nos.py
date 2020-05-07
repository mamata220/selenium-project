num1 = input("Enter two number: ")
num2 = num1.split(" ")
x1 = int(num2[0])
x2 = int(num2[1])


def substract(x, y):
    if x < y:
        output = y - x
    else:
        output = x - y
    return output


print(substract(x1, x2))
