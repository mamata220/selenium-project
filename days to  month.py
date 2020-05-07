age = input("enter your age in years and months ")
age_split = age.split(" ")
print(age_split)
age_years = int(age_split[0])
age_months = int(age_split[1])
age_days = int(age_split[2])
age_yearsindays = age_years * 365
age_monthsindays = age_months*30

print(f"Your age in days : "+str(age_yearsindays+age_monthsindays+age_days))
