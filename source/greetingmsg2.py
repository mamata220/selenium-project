name = input("Enter your Name :")
time1 = input("Enter the current time as AM or PM, Ex: 11 pm :")
splitted_time = time1.split(" ")
entered_time = splitted_time[0]
am_pm = splitted_time[1]

entered_time_int = int(entered_time)
greetmsg = "Welcome {}"

if am_pm.upper() == "AM":
    if 12 == entered_time_int:
        greetmsg = "Good Night, {}"
    elif 1 == entered_time_int:
        greetmsg = "Good Night, {}"
    elif 2 <= entered_time_int <= 4:
        greetmsg = "Go to bed {}, it's too late already."
    elif 5 <= entered_time_int <= 11:
        greetmsg = "Good morning, {}"

elif am_pm.upper() == "PM":
    if 12 == entered_time_int:
        greetmsg = "Good noon, {}"
    if 1 == entered_time_int:
        greetmsg = "Good noon, {}"
    elif 2 <= entered_time_int <= 4:
        greetmsg = "Good Afternoon, {}"
    elif 5 <= entered_time_int <= 9:
        greetmsg = "Good evening, {}"
    elif 10 <= entered_time_int <= 11:
        greetmsg = "Good night, {}"

print(greetmsg.format(name))