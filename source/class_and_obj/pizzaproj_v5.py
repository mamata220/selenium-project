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
        self.veg_toppings_avl_list = ["tomato", "onion", "capsicum", "corn", "jalapino", "mushroom"]
        self.nonveg_toppings_avl_list = ["chicken", "pepproni", "shrimp"]
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

    def check_veg_topping_availability(self, topping):
        is_topping_found = False

        if topping in self.veg_toppings_avl_list:
            is_topping_found = True
        return is_topping_found

    def nonveg_toppings_selected_from_avl_list(self, user_chosen_toppings):
        nonveg_toppings_found_set = {}
        nonveg_toppings_avl_list_as_set = set(self.nonveg_toppings_avl_list)

        if "," in user_chosen_toppings:
            toppings_list_from_user = user_chosen_toppings.split(",")
            toppings_list_from_user = [topping.strip() for topping in toppings_list_from_user]
            toppings_list_set_from_user = set(toppings_list_from_user)

            nonveg_toppings_found_set = nonveg_toppings_avl_list_as_set.intersection(toppings_list_set_from_user)
        else:
            nonveg_toppings_found_set = nonveg_toppings_avl_list_as_set.intersection(user_chosen_toppings)

        return nonveg_toppings_found_set

    """def check_if_nonveg_chosen_has_nonveg_topping(self, user_chosen_toppings):
        nonveg_toppings_found_set = {}
        nonveg_toppings_avl_list_as_set = set(self.nonveg_toppings_avl_list)

        #if self.veg_nonveg.lower() == "non-veg" or self.veg_nonveg.lower() == "nonveg":
        if "," in user_chosen_toppings:
            toppings_list_from_user = user_chosen_toppings.split(",")
            toppings_list_from_user = [topping.strip() for topping in toppings_list_from_user]
            toppings_list_set_from_user = set(toppings_list_from_user)

            nonveg_toppings_found_set = nonveg_toppings_avl_list_as_set.intersection(toppings_list_set_from_user)
        else:
            nonveg_toppings_found_set = nonveg_toppings_avl_list_as_set.intersection(user_chosen_toppings)

        return nonveg_toppings_found_set"""

    def check_topping_available_in_stock(self, topping):
        is_topping_found = False

        if self.veg_nonveg.lower() == "veg":
            is_topping_found = self.check_veg_topping_availability(topping)
        elif self.veg_nonveg.lower() == "non-veg" or self.veg_nonveg.lower() == "nonveg":
            if topping in self.nonveg_toppings_avl_list:
                is_topping_found = True

            if not is_topping_found:
                is_topping_found = self.check_veg_topping_availability(topping)

        return is_topping_found

    def check_veg_nonveg_topping_added_correctly(self, user_chosen_toppings):
        nonveg_toppings_found_set = self.nonveg_toppings_selected_from_avl_list(user_chosen_toppings)

        if self.veg_nonveg.lower() == "non-veg" or self.veg_nonveg.lower() == "nonveg":
            if not (len(nonveg_toppings_found_set) > 0):
                print(
                    f"You have chosen {self.veg_nonveg} pizza, but not added any non-veg topping(s): {nonveg_toppings_found_set}, please correct your order.")
                self.add_toppings()
        elif self.veg_nonveg.lower() == "veg":
            if len(nonveg_toppings_found_set) > 0:
                print(
                    f"You have chosen {self.veg_nonveg} pizza, but added non-veg topping(s): {nonveg_toppings_found_set}, please correct your order.")
                self.add_toppings()

    def check_toppings_availability(self, user_chosen_toppings):

        user_toppings_not_found_list = []

        if "," in user_chosen_toppings:
            toppings_list_from_user = user_chosen_toppings.split(",")

            for each_topping in toppings_list_from_user:
                each_topping_without_spaces = each_topping.strip()
                is_topping_avl = self.check_topping_available_in_stock(each_topping_without_spaces)
                if not is_topping_avl:
                    user_toppings_not_found_list.append(each_topping_without_spaces)
        else:
            is_topping_avl = self.check_topping_available_in_stock(user_chosen_toppings.strip())
            if not is_topping_avl:
                user_toppings_not_found_list.append(user_chosen_toppings.strip())

        return user_toppings_not_found_list

    def add_toppings(self):
        user_input_toppings = input(f"Add your toppings for your '{self.veg_nonveg}' pizza (comma separated): ")
        self.check_veg_nonveg_topping_added_correctly(user_input_toppings)
        topping_not_found_list = []
        topping_not_found_list = self.check_toppings_availability(user_input_toppings)
        if len(topping_not_found_list) > 0:
            print(f"{topping_not_found_list} toppings you chosen, not available in our stock.")
            print("Please choose different toppings!")
            print()
            user_input_toppings = self.add_toppings()

        return user_input_toppings

    def get_pizza_details_from_user(self):
        self.size = self.get_correct_pizza_size()

        self.crust = self.get_correct_crust()

        self.type = input("Pan or Handmade ? ")
        self.veg_nonveg = input("Veg or Non-Veg ? ")

        self.user_toppings = self.add_toppings()

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
