def isPalindrome(str):  # ABCBA
    reverse_str = reverse(str)
    #print(reverse_str)
    result = False
    if reverse_str == str:
        #print("true")
        result = True
    else:
       # print("false")
       result = False


    return result



# Python code to reverse a string
# using extended slice syntax

# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string


print(isPalindrome("wow"))
