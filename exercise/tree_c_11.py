def print_pattern_01(max):
    #max = 12
    if type(max) == int:
        if max == 0:
            max = 8
        for num in range(0, max):
            print("0" * num)
    else:
        print("Please provide an integer value")




print("Hello, what are you looking for")