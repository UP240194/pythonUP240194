#dia 6 level 1 y 2 

#ejercicio 1 
empty_tuple = ()

#ejercicio 2
Names_M = ("Fer","Israel",)
Names_F = ("Hanna","Juana")
print(f"{Names_M}\n{Names_F}")

#ejercicio 3
Names = Names_M+Names_F
print(Names)

#ejercicio 4 
brothers = ("Fer","Israel")
print(brothers)

#ejercicio 5 
parents = ("Aleberto","Ana")
print(parents)
family_members = brothers+parents
print(family_members)

#level 2 

#ejercicio 1 
brothers = family_members[:2]
parents = family_members[-2:]
print(f"{brothers}\n{parents}")

#ejercicio 2
fruits = ("Banana","Coco","Piña")
vegetables = ("cebolla","elote","Papa")
animal_products = ("leche","queso","mantequilla")
food_stuff_tp = fruits+vegetables+animal_products
print(f"{fruits}\n{vegetables}\n{animal_products}")
print(food_stuff_tp)

#ejercicio 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#ejercicio 4
middle = len(food_stuff_lt)//2
print(food_stuff_lt[middle])

#ejercicio 5
print(f"{food_stuff_lt[0]}, {food_stuff_lt[1]}, {food_stuff_lt[3]}")

#ejericico 6 
del food_stuff_tp

#ejercicio 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
check = "Estonia" in nordic_countries
print(check)
check = "Iceland" in nordic_countries
print(check)

