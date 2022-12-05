height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

w = float(weight)
h = float(height)
BMI = (w/(h ** 2))
BMI_int = int(BMI)
print(BMI_int)
