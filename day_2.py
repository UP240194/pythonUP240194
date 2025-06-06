first_name=input('¿Cual es tu nombre?')
last_name=input('¿Cual es tu primer apellido?')
full_name=('Ximena Ruiz')
country=('¿Cual es tu pais de procedencia?')
city='Ags'
age=input('¿Cual es tu edad?')
year=2006
is_married,is_true,is_light_on=True,True,True

#Checking data types
print('Data types d')
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#length of first name
first_name_length=(len(first_name))

#comparing lengths
comparing_length= len(last_name)
print(first_name_length,'-',len(last_name),'=',comparing_length)

#declaring numbers
num_one=5
num_two=4

#declating operations
total= num_one + num_two
diff= num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder= num_one%num_two
esx=num_one**num_two
floor_division= num_one//num_two

#circle area
radius=int(input('escribe el valor del radio para calcular el area y circunferencia de un circulo:'))
area_of_circle=3.14*(radius**2)
circum_of_circle=3.14*(2*radius)
print(circum_of_circle)