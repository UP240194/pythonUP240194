#level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"It companies: {it_companies}")

#ejercicio 1
print(len(it_companies))

#ejercicio 2 
it_companies.add("Twitter")
print(it_companies)

#ejercicio 3 
it_companies.update(["YouTube","Android","Lenovo"])
print(it_companies)

#ejercicio 4 
it_companies.remove("Apple")
print(it_companies)

#level 2 

#ejercicio 1 
print(f"A: {A}")
print(f"B: {B}")

#ejercicio 2 
print(A.intersection(B))

#ejercicio 3
print(A.issubset(B))

#ejercicio 4
print(A.isdisjoint(B))

#ejercicio 5 
A.update(B)
B.update(A)

print(f"A: {A}")
print(f"B: {B}")

#ejercicio 6
print(A.symmetric_difference(B))

#ejercicio 7
del A
del B


#level 3 

#ejercicio 1
st_ages = set(age)
print(len(age))
print(len(st_ages))

#ejercicio 2
#string: es una cadena de caracteres que almacena texto y es inmodificable.
#list: es un conjunto de elementos que pueden ser de diferentes tipos y se pueden modificar y utiliza [].
#tuple: es simlar a una lista pero es inmodificable y se utiliza ().
#set: es un conjunto de elementos únicos y no ordenados, se utiliza {}.

#ejercicio 3 
oracion = "I am a teacher and I love to inspire and teach people"
palabras = oracion.split()
palabras_unicas = set(palabras)
print(palabras_unicas)
print(len(palabras_unicas))

