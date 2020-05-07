class Pizza:
    def __init__(self, pizza_dim, crust_size, type_of_pizza, veg_nonveg):
        self.dimension = pizza_dim
        self.crust = crust_size
        self.pizzatype = type_of_pizza
        self.veg_nonveg = veg_nonveg


    def veg_ingredient(ings):
        ingredients_veg_list = ["tomato", "onion", "capsicum", "corn", "jalapino", "mushroom"]
        is_user_ings_availabile_in_list = False

        for i in ingredients_veg_list:
            if i == ings:
                is_user_ings_availabile_in_list = True
                print(ings, " is available")
                break

        if is_user_ings_availabile_in_list == False:
            print("ingredient is not available")



    @staticmethod
    def nonveg_ingredient(ings):
        ingredients_nonveg = ["chicken", "peporoni", "chicken_grilled"]
        for i in ingredients_nonveg:

            print(i)

        else:
            print("ingredient is not available")

    """ @staticmethod
    def veg_ingredient(x):
        ingredient =["t","c","o"]
        while True:
            if x == ingredient:
                print(x)
                break
            else:
                print("ingredient is not available")"""
