import time


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
        self.user_name = input("Please enter your name: ")

    veg_toppings_av_list = ["tomato", "onion", "capsicum", "corn", "jalapino", "mushroom"]
    nonveg_toppings_av_list = ["chicken", "pepproni", "shrimp"]

    def get_pizza_details_from_user(self):

        self.size = int(input("Pizza size (8 or 12 or 16 or 20)? "))
        self.crust = input("Crust type (thin or thick)? ")
        self.type = input("Pan or Handmade ? ")
        self.veg_nonveg = input("Veg or Non-Veg ? ")
        self.user_toppings = input(f"Add your toppings for your '{self.veg_nonveg}' pizza (comma separated): ")

    """def 

    def check_topping_availability(self, user_choosen_toppings):

        toppings_list_from_user = user_choosen_toppings
        
        if "," in user_choosen_toppings:
            toppings_list_from_user  = user_choosen_toppings.split(",")
            
    
        
        for toppings_list_from_user 
            
            
        for  in ingredients_veg:
            if i == ings:
                print(i)

            else:
                print("ingredient is not available")
                
"""

    def bake_user_pizza(self):
        pizza = Pizza(self.size, self.crust, self.type, self.veg_nonveg, self.user_toppings)

        return pizza

    def take_pizza_order(self):

        self.get_pizza_details_from_user()
        print()
        print("We received your Pizza order as below: ")
        print(
            f"Size chosen {self.size} in, {self.crust} crust, {self.veg_nonveg}, {self.type} with '{self.user_toppings}' topping(s)")

        user_confiramation = input("Please confirm your order (Yes : Y, No : N) : ")
        if (user_confiramation.upper() == "Y") or (user_confiramation.upper() == "YES"):
            print("Thanks for confirming your order")
            print("Your pizza is being bake now.. please wait for some time..")
            self.bake_user_pizza()
            time.sleep(5)  # time taking to making pizza
            print(f"Hello {self.user_name}, your pizza is ready now. Enjoy!")
        elif (user_confiramation.upper() == "N") or (user_confiramation.upper() == "NO"):
            print()
            print("Please enter the details again: ")
            self.take_pizza_order()
        else:
            print()
            print("Invalid choices made. Sorry, no Pizza for you!")
