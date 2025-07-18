#nivel 1 dia 9

#ejercicio 1 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")

#ejercicio 2
my_age = 25                                 
your_age = int(input("Enter your age: "))

if your_age > my_age:
    age_difference = your_age - my_age
    year_text = "year" if age_difference == 1 else "years"
    print(f"You are {age_difference} {year_text} older than me.")
elif your_age == my_age:
    print("We are the same age.")
else:
    age_difference = my_age - your_age
    year_text = "year" if age_difference == 1 else "years"
    print(f"I am {age_difference} {year_text} older than you.")

#ejercicio 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")