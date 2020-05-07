def lower_case_checker():
    user_str = input("Enter a string : ")
    upper_list = [] #""
    lower_list= []
    number_list =[]
    for str in user_str:


        if str.isupper():
            upper_list.append(str)
            #upper_list = upper_list + ",  " + str
        elif str.islower():
            lower_list.append(str)
        elif str.isdigit():
            number_list.append(str)

    upper_list_as_str = ", ".join(upper_list)
    lower_list_as_str = ",  ".join(lower_list)

    #print(f"Upper ch found: {upper_list} and Lower ch found: {lower_list} \n Found number: {number_list}")
    print(f"Upper ch found: {upper_list_as_str} \nLower ch found: {lower_list_as_str} \nFound numbers: {number_list}")


lower_case_checker()
