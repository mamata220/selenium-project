import math


class BasicCal:
    def __init__(self, make, model, usage):
        self.make = make
        self.model = model
        self.usage = usage

    def addition(self, x, y):
        return x + y

    def substraction(self, y, z):
        return y - z

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def percentage(self, x, y):
        return x * y * .01

    def print_oeration_result(self, str_data):

        result = 0
        operation_str = ""

        if "+" in str_data:
            x, y = str_data.split("+")

            x = int(x.strip())
            y = int(y.strip())

            operation_str = "Sum"
            result = self.addition(x, y)

        elif "-" in str_data:
            x, y = str_data.split("-")

            x = int(x.strip())
            y = int(y.strip())

            operation_str = "Substraction"
            result = self.substraction(x, y)

        elif "*" in str_data:
            x, y = str_data.split("*")

            x = int(x.strip())
            y = int(y.strip())

            operation_str = "Multiplication"
            result = self.multiplication(x, y)

        elif  "/" in str_data:
            x, y = str_data.split("/")

            x = int(x.strip())
            y = int(y.strip())

            operation_str = "Division"
            result = self.division(x, y)

        print(f"{operation_str} result = {result}")






class ScFiCal(BasicCal):

    @staticmethod
    def get_sin_as_radian(x):
        y = math.sin(x)
        return y

    @staticmethod
    def get_sin_as_degree(x):
        x_as_degree = math.degrees(x)
        return math.sin(x_as_degree)

    def get_cos(self, x):
        y = math.cos(x)
        return y

    def sq_root(self, x):
        y = math.sqrt(x)
        return y

    def get_tan(self,x):
        y = math.tan(x)
        return y
