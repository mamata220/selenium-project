
def get_extension_oneway(filename):

    file_ext = filename.split(".")
    #filename_part = file_ext[0]
    ext_part = file_ext[1]
   #full_extension = "." + ext_part

    return "." + ext_part


def get_extension_anotherway(filename):

   index_of_dot  = filename.find(".")
   #print(index_of_dot)
   extension_part = filename[filename.find(".") : ]
   #print(extension_part)

   return extension_part

print(get_extension_anotherway("Greetings.jpg"))
print(get_extension_anotherway("Some.pdf"))
print(get_extension_anotherway("somesong.mp3"))








"""print(get_extension_oneway("Greetings.jpg"))
print(get_extension_oneway("OfferLetter.pdf"))
print(get_extension_oneway("mysong.mp3"))
print(get_extension_oneway("invoicesheet.xlsx"))
"""