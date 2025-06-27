#ejercicio 1 
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
resultado = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(resultado)

#ejercicio 2
string1 = 'Coding'
string2 = 'For'
string3 = 'All'
resultado = string1 + ' ' + string2 + ' ' + string3
print(resultado)

#ejercicio 3
company = "coding For All"

#ejercicio 4
print(company)

#ejercicio 5
company = "Coding For All"
print(len(company))

#ejercicio 6
company = "Coding For All"
company_upper = company.upper()
print(company_upper)

#ejercicio 7
company = "Coding For All"
company_lower = company.lower()
print(company_lower)

#ejercicio 8
cadena = "Coding For All"
cadena_capitalizada = cadena.capitalize()
print(cadena_capitalizada)
cadena = "Coding For All"
cadena_titulo = cadena.title()
print(cadena_titulo)
cadena = "Coding For All"
cadena_invertida = cadena.swapcase()
print(cadena_invertida)

#ejercicio 9
company = "Coding For All"
palabras = company.split() 
primera_palabra = palabras[0] 
print(primera_palabra)

#ejercicio 10
company = "Coding For All"
try:
    company.index("Coding")
    print("La palabra 'Coding' se encuentra en la cadena ")
except ValueError:
    print("La palabra 'Coding' no se encuentra en la cadena ")

#ejercicio 11
original_string = "Coding For All"
new_string = original_string.replace("Coding", "Python")
print(new_string)

#ejercicio 12
original_string = "Python For All"
new_string = original_string.replace("All", "Everyone")
print(new_string)

#ejercicio 13
string = 'Coding For All'
lista_de_palabras = string.split()
print(lista_de_palabras)

#ejercicio 14
cadena_empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_empresas = [empresa.strip() for empresa in cadena_empresas.split(',')]
print(lista_empresas)

#ejercicio 15
string = "Coding For All"
caracter_en_0 = string[0]
print(caracter_en_0)

#ejercicio 16
cadena = "Coding For All"
longitud_cadena = len(cadena)
ultimo_indice = longitud_cadena - 1
print(ultimo_indice)

#EJERCICIO 17
print(company[10])

#ejercicio 18
company_python_split = company_python.split()

Primera = company_python_split[0][0]
Segunda = company_python_split[1][0]
Tercera = company_python_split[2][0]

print(f"{Primera+Segunda+Tercera}")

#ejercicio 19
company_split = company.split()

Primera = company_split[0][0]
Segunda = company_split[1][0]
Tercera = company_split[2][0]

print(f"{Primera+Segunda+Tercera}")

#ejercicio 20
print(company.find("C"))

#ejercicio 21
print(company.find("F"))

#ejercicio 22
single_string_3 = company+people

print(single_string_3.rfind("l"))

#ejercicio 23
single_string_4 = "You cannot end a sentence with because because because is a conjunction"
print(f"\noriginal text:\n{single_string_4}")
position_because = single_string_4.find("because")
print(f"\nfirst occurrence of because in the sentence = {position_because}")

#ejercicio 24
position_because = single_string_4.rfind("because")
print(f"\nlast occurrence of because in the sentence = {position_because}")

#ejercicio 25
print("\ntext whiuot because :")
print(single_string_4[:31]+single_string_4[55:])   

#ejercicio 26
position_because = single_string_4.find("because")
print(f"\nfirst occurrence of because in the sentence = {position_because}")

#ejercicio 27
print("\ntext whiuot because :")
print(single_string_4[:31]+single_string_4[55:])

#ejercico 28
question_1 = company.startswith("Coding")
print(f"\nDoes ''Coding For All' start with a substring Coding? R: {question_1}")

#ejercicio 29
question_2 = company.endswith("coding")
print(f"\nDoes ''Coding For All' end with a substring Coding? R: {question_2}")

#ejercicio 30
single_string_5 = '   Coding For All      '
print("\nleft and right trailing spaces of '   Coding For All      '")
print(single_string_5.strip())

#ejercicio 31
print("\n30DaysOfPython whit isidentifier is")
print("30DaysOfPython".isidentifier())
print("\nthirty_days_of_python with isidentifier is")
print("thirty_days_of_python".isidentifier())

#ejercicio 32
print("\nlist: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']")
print("\nJoin the list with a hash with space string")
print(" # ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

#ejercicio 33
print("\nI am enjoying this challenge.\nI just wonder what is next.")

#ejercicio 34
print("\nName     \tAge   \tCountry   \tCity")
print("Asabeneh \t250   \tFinland   \tHelsinki")

#ejercicio 35
radius = 10
area = 3.14 * radius ** 2
print(f"\nThe area of a circle with radius {radius} is {area} meters square.")

#ejercicio 36
a, b = 8, 6
print(f"\n{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}\n{a} % {b} = {a%b}\n{a} // {b} = {a//b}")
print(f"{a} * {b} = {a*b}")
