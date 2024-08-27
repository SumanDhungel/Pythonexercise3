age = float(input("Enter your age: "))
weight = float(input("Enter your weight: "))
if age >= 18:
    print("Medicine can be administered")
if 18 > age >= 15 and weight >= 55:
    print("Medicine can be administered")
elif 18 > age >= 15 and weight < 55 or age < 15:
    print("Medicine can not be administered")
score = int(input("Enter your score: "))
if score >= 90:
    print("A1")
elif score >= 80:
    print("A2")
elif score >= 70:
    print("B1")
elif score >= 60:
    print("B2")
elif score >= 50:
    print("C1")
elif score >= 35:
    print("C2")
elif score < 35:
    print("fail")
wheels = int(input("Enter number of wheels: "))
battery = str(input("Enter if it has a battery - Yes/No: "))
if wheels ==2 and battery == "Yes":
    print("It is an electric bicycle")
elif wheels ==2 and battery == "No":
    print("It is a bicycle")
if wheels ==3 and battery == "Yes":
    print("It is an electric tricycle")
elif wheels ==3 and battery == "No":
    print("It is a tricycle")
if wheels ==4 and battery == "Yes":
    print("It is an electric car")
elif wheels ==4 and battery == "No":
    print("It is a car")

age = int(input("Enter your age: "))
if age >= 65:
    print("Retire")
elif age>=18:
    print("Working age")
elif age>= 7:
    print("Studying")
elif age >= 0:
    print("Child")
