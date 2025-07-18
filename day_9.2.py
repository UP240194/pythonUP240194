#nivel 2 dia 9

#ejercicio 1
score = int(input("Enter your score: "))

if 80 <= score <= 100:      
    print("Grade: A")  
elif 70 <= score < 80:
    print("Grade: B")
elif 60 <= score < 70:
    print("Grade: C")
elif 50 <= score < 60:
    print("Grade: D")
elif 0 <= score < 50:
    print("Grade: F")

#ejercicio 2 
month = input("Enter the name of a month: ")

if month in ["September", "October", "November"]:   
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:  
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("That is not a valid month.")  

#ejercicio 3 
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")

if fruit not in fruits:
    print(fruit, "is not in the list")      
    print("Adding fruit to the list")       
    fruits.append(fruit)                   
    print("Modified list:", fruits)         
else:
    print("That fruit already exist in the list")