import time
import re


class Pizza:
    def __init__(self, pizza_dim, crust_size, type_of_pizza, veg_nonveg, usr_toppings):
        self.dimension = pizza_dim
        self.crust = crust_size
        self.pizza_type = type_of_pizza
        self.veg_nonveg = veg_nonveg
        self.toppings = usr_toppings


class PizzaHut:

    def __init__(self):
        self.size = 8
        self.crust = "thick"
        self.type = "handmade"
        self.veg_nonveg = "nonveg"
        self.user_toppings = "chicken"
        self.customer_name = ""
        self.veg_toppings_av_list = ["tomato", "onion", "capsicum", "corn", "jalapino", "mushroom"]
        self.nonveg_toppings_av_list = ["chicken", "pepproni", "shrimp"]
        self.sizes_available = (8, 12, 16, 20)
        self.correct_crust = ["thin", "thick"]
        self.correct_type = ["pan", "handmade"]

    def get_customer_name(self):
        cust_name = input("Please enter your name: ")
        reg_expression_pattern = '[A-z]'
        is_correct_cust_name = bool(re.match(reg_expression_pattern, cust_name))

        if not is_correct_cust_name:
            print("Name entered is invalid, only alphabets allowed.")
            cust_name = self.get_customer_name()

        return cust_name

    def get_correct_crust(self):
        input_crust = (input("Crust type (thin or thick)? ")).lower()
        if input_crust not in self.correct_crust:
            print("Invalid input, please re-enter crust .")
            input_crust = self.get_correct_crust()

        return input_crust

    def get_correct_pizza_size(self):
        size = int(input("Pizza size (8 or 12 or 16 or 20)? "))
        if size not in self.sizes_available:
            print("opted size is not available,please re-enter size.")
            size = self.get_correct_pizza_size()

        return size

    def get_pizza_details_from_user(self):
        self.size = self.get_correct_pizza_size()

        self.crust = self.get_correct_crust()

        self.type = input("Pan or Handmade ? ")
        self.veg_nonveg = input("Veg or Non-Veg ? ")
        self.user_toppings = input(f"Add your toppings for your '{self.veg_nonveg}' pizza (comma separated): ")

    def bake_user_pizza(self):
        pizza = Pizza(self.size, self.crust, self.type, self.veg_nonveg, self.user_toppings)

        return pizza

    def take_pizza_order(self):
        if self.customer_name == "":
            self.customer_name = self.get_customer_name()

        self.get_pizza_details_from_user()
        print()
        print("We received your Pizza order as below: ")
        print(
            f"Size chosen {self.size} in, {self.crust} crust, {self.veg_nonveg}, {self.type} with '{self.user_toppings}' topping(s)")

        user_confirmation = input("Please confirm your order (Yes : Y, No : N) : ")
        if (user_confirmation.upper() == "Y") or (user_confirmation.upper() == "YES"):
            print("Thanks for confirming your order")
            print("Your pizza is being bake now.. please wait for some time..")
            self.bake_user_pizza()
            time.sleep(5)  # time taking to making pizza
            print(f"Hello {self.customer_name}, your pizza is ready now. Enjoy!")
        elif (user_confirmation.upper() == "N") or (user_confirmation.upper() == "NO"):
            print()
            print("Please enter the details again: ")
            self.take_pizza_order()
        else:
            print()
            print("Invalid choices made. Sorry, no Pizza for you!")
