print("--- Age in days calculator ---")
age_years = input ("Enter your age in years : ")
age_years = int(age_years)
age_days = age_years*365
print(f"You have lived for : {age_days} Dasys.")
age_months = age_years*12
print (f"You have lived for : {age_months} Months.")
age_hours = age_years*3456
print (f"You have lived for : {age_hours} hours.")
age_minutes = age_years*age_months*age_days*age_hours*60
print (f"You have lived for : {age_minutes} minutes.")
age_seconds = age_years*age_months*age_days*age_hours*60
print(f"You have lived for : {age_seconds} seconds.")
