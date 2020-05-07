#value1 = int(input("enter first number"))
#value2 = int(input("Enter second number"))
value = input("Enter two number separated by space: ")
value2 = value.split(" ")
x1 = int(value2[0])
y1 = int(value2[1])



def sum_of_two_num(x, y):
    sum1 = x + y
    return sum1


print(sum_of_two_num(x1, y1))