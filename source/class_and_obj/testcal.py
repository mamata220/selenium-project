from source.class_and_obj.calculatorprog import BasicCal, ScFiCal

"""
calculation = BasicCal("casio", "sd34", "calculation")
print("sum =", calculation.addition(5, 7))
print("substraction = ",calculation.substraction(5,4))
print("mul=",calculation.multiplication(3, 4))
print("div=",calculation.division(6, 2))
print("percentage =",calculation.percentage(100, 10))


scical1 = ScFiCal("casio", "sd45", "scical")
print("get_sin_as_radian=", ScFiCal.get_sin_as_radian(90)) #calling a static method,so using the class name to call the method
print("get_sin_as_degree=", ScFiCal.get_sin_as_degree(90)) #calling a static method,so using the class name to call the method
print("get_cos=", scical1.get_cos(90)) #instance method becauseusing self parameter we haveto create obj to call it
print("get_sqrt=", scical1.sq_root(81))
print("get_tan=", scical1.get_tan(90))

"""
str_inp = input("Please enter two values to do the basic calculation,  \nfor example: 2 + 3 to get addition and press q to quit: ")
cal1 = BasicCal("casio", "sd34", "calculation")
cal1.print_oeration_result(str_inp)



