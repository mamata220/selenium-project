def sum_of_three(arg1, arg2, arg3):
    sum1 = arg1 + arg2 + arg3

    if (arg1 == arg2) or (arg2 == arg3) or (arg3 == arg1):
        sum1 = sum1 * 2

    return sum1

print(sum_of_three(5, 5, 5)) #30
print(sum_of_three(4, 6, 4)) # 28
print(sum_of_three(5, 22, 1)) # 28
print(sum_of_three(3, 7, 3)) #26

