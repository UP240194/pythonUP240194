#ejercicio 1
empty_list = list()
print(f"empty list = {empty_list}")

#ejercicio 2 
new_list_games = ["Fortnite", "GTA V", "Street fighter", "God of war", "Borderlands", "Fallout"]
print(f"new list = {new_list_games}")

#ejercicio 3
print(f"length of games list = {len(new_list_games)}")

#ejercicio 4 
print(f"firts item = {new_list_games[0]}")
print(f"last item = {new_list_games[-1]}")
middle = (len(new_list_games)+1)//2
print(f"middle item = {new_list_games[middle]}")

#ejercico 5
mixed_data_types = ["Jorge", 20, 1.69, "single", "Aguascalientes"]
print(f"\nmixed data types = {mixed_data_types}")

#ejercicio 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#ejercico 7
print(f"\ncomanies list = {it_companies}")

#ejercicio 8
print(f"length of companies list = {len(it_companies)}")

#ejercico 9 
print(f"firts item = {it_companies[0]}")
print(f"last item = {it_companies[-1]}")
middle = (len(it_companies)+1)//2
print(f"middle item = {it_companies[middle]}")

#ejerccio 10
it_companies[1] = "Gugle"
print(f"\nchange in companies list\n= {it_companies}")

#ejercicio 11
it_companies.append("Linux")
print(f"\nadd an IT company (Linux)\n= {it_companies}")

#ejercicio 12
middle = len(it_companies)//2
it_companies.insert(middle,"Android")
print(f"\ninsert an IT company in the middle\n= {it_companies}")

#ejercicio 13
it_companies[4] = it_companies[4].upper()
print(f"\nchange one name to uppercase\n= {it_companies}")

#ejercicio 14
print(f"\njoin the hash at the companies list")
print("= ","#; ".join(it_companies))

#ejercicio 15
print("\nis IBm in the companies list?")
print("IBM" in it_companies)
print("is Google in the companies list?")
print("Google" in it_companies)

#ejercicio 16
it_companies.sort()
print(f"\ncompanies list sort\n= {it_companies}")

#ejercico 17
it_companies.reverse()
print(f"\nreverse companies list\n= {it_companies}")

#ejercicio 18
first_3 = it_companies[:3]
print(f"\nthe first companies are\n= {first_3}")

#ejercicio 19 
last_3 = it_companies[-3:]
print(f"\nthe last companies are\n= {last_3}")

#ejercicio 20
middle = (len(it_companies)+1)//2
print(f"\nthe comany or companies in the middle are\n= {it_companies[middle:middle+1]}")

#ejercicio 21
del it_companies[0]
print(f"\nremove the firts item in companies list\n= {it_companies}")

#ejercicio 22
middle = len(it_companies)//2
del it_companies [middle:middle+1]
print(f"\nremove the middle item in companies list\n= {it_companies}")

#ejercicio 23
del it_companies[-1]
print(f"\nremove the last item in companies list\n= {it_companies}")

#ejercicio 24
del it_companies[:]
print(f"\nremove al items in companies list\n= {it_companies}")

#ejercicio 25
del it_companies
print(f"\ndestroy the companies list")

#ejercicio 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
print(f"\njoin {front_end} + {back_end}\n= {join}")

#ejercicio 27
full_stack = join
redux = full_stack.index("Redux")
position = redux+1
full_stack[position:position] = ["Python", "SQL"]
print(f"\njoin Python and SQL after Redux\n={full_stack}")
