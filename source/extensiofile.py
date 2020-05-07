def filename(f_extension):
    #temp = f_extension.split(".")
    temp = f_extension.split(".")
    extension_var = temp[0]
    extension_var2 = temp[1]
    extension = extension_var +"."+extension_var2


    return extension

print(filename("gana.com"))