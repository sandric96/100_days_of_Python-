age = input("What is your current age? ")
age_int = int(age)

years = 100 - age_int
days = years *365
weeks= years *52
months = years *12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
