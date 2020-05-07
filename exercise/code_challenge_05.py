def hello_user(f_name, l_name, gender):
    result = ""
    if gender == "male":
        result = "Hello Mr " + f_name + " " + l_name
    elif gender == "female":
        result = "Hello Mrs "+f_name + " " + l_name

    return result


value = hello_user("Muna", "sahoo", "male")
print(value)

print(hello_user("Sanghamitra", "Sahoo", "female"))









