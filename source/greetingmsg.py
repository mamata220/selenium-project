import time
#import datetime
name = input("Enter your Name :")
#print(name)
time1 = input("Enter the current time :")
splitted_time = time1.split(" ")
entered_time = splitted_time[0]
am_pm = splitted_time[1]
#print(entered_time)
#print(am_pm)

entered_time_int = int(entered_time)

after12pm = 12

if am_pm.upper() == "AM":
    if 5 <= entered_time_int <= 11:
        print("Good morning, " + name)
    elif 12 == entered_time_int:
        print("Good Night, " + name)
    elif 1 == entered_time_int:
        print("Good Night, " + name)
    elif 2 <= entered_time_int <= 4:
        print("Go to bed, " + name + " it's too late already.")

elif am_pm.upper() == "PM":
    if 12 <= entered_time_int <= 13:
        print("Good noon:" + name)
    elif 14 <= entered_time_int <= 16:
        print("Good Afternoon:" + name)
    elif 17 <= entered_time_int <= 21:
        print("Good evening:" + name)
    elif 22 <= entered_time_int <= 23:
        print("Good night:" + name)