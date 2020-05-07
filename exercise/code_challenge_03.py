def sum_of_three(arg1, arg2, arg3):

    sum1 = arg1 + arg2 + arg3

    if (arg1 == arg2) or (arg2 == arg3) or (arg3 == arg1):
        try:
            sum1 = sum1 * 2
        except TypeError:
            print("Some error happened, error is ")

    return sum1


