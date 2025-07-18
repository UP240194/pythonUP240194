#ejercicio 1 
dog = {}

#ejercicio 2 
dog = {"name": "Mila", "color": "White", "breed": "Samoyedo", "legs": 4, "age": 5}
print(f"Dog = {dog}")

#ejercicio 3
student = {"first_name": "Ximena", "last_name": "Ruiz ", "gender": "F", "age": 19, "marital_status": "single", "skills": "programming", "country": "Mexico", "city": "Aguascalientes", "address": "Av. Independencia"}
print(f"\nstudent = {student}")

#ejercicio 4 
print(f"\nlength of student dictionary = {len(student)}")

#ejercicio 5
print(f"\nskills = {student['skills']}")

#ejercicio 6
student["skills"] = ["programming","Python"]
print(f"\nModified skills = {student['skills']}")

#ejercicio 7
print(f"\nKeys of student dictionary = {list(student.keys())}")

#ejercicio 8
print(f"\nValues of student dictionary = {list(student.values())}")

#ejercicio 9
student_items = list(student.items())
print(f"\nStudent items as list of tuples = {student_items}")

#ejercicio 10
del student["marital_status"]
print(f"\nStudent dictionary after deletion = {student}")

#ejercicio 11
del dog
print("\nDog dictionary has been deleted.")