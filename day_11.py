#dia once nivel 1 

#ejercicio 1 
print()
def add_two_numbers(a,b):
    return a + b

print(add_two_numbers(3, 5))

#ejercicio 2 
print()
def area_of_circle(r):
    return 3.1416 * r * r
print(area_of_circle(4))

#ejercicio 3 
print()
def add_all_nums(*args):                                        
    if not all(isinstance(arg, (int, float)) for arg in args):  
        return "All arguments must be numbers."                 
    total = 0                                                   
    for arg in args:                                            
        total += arg                                            
    return total                                                
print(add_all_nums(2, 3, 5)) 

#ejercicio 4
print()
def convert_celsius_to_fahrenheit(c):
    return(c * 9/5) + 32
print(convert_celsius_to_fahrenheit(50))

#ejercicio 5
print()
def check_season(month):

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

check_season("March")

#ejercicio 6
print()
def calculate_slope(x1,y1,x2,y2):
    rest_y = y2 - y1
    rest_x = x2 - x1
    if rest_x == 0:
        return "slope is undef."
    else:
        return rest_y / rest_x

print(calculate_slope(2,3,4,5))

#ejericico 7
print()
def solve_quadratic_eqn(a,b,c):
    if a == 0:
        return "a cannot be a zero"
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "no real solution"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"one solution: x = {x}"
    else:
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return f"two solutions: x_1 = {x1}, x_2 = {x2}"

print(solve_quadratic_eqn(1,-3,2))

#ejercicio 8 
print()
def print_list(list):
    for item in list:
        print(item)

print_list([1,2,3,4,5,6])

#ejerciico 9 
print()
def reverse_list (list):
    reverse_elems = []
    for i in range(len(list)-1,-1,-1):
        reverse_elems.append(list[i])
    return reverse_elems

print(reverse_list([1, 2, 3, 4, 5, 6]))


#ejerciico 10 
print()
def capitalize_list_items(list):
    capt_items = []
    for item in list:
        if isinstance(item, str):
            capt_items.append(item.capitalize())
    else:
        try:
            str_item = str(item)
            capt_items.append(str_item.capitalize())
        except Exception as e:
            capt_items.append("error")
    return capt_items

print(capitalize_list_items(["hola","konnichiwa","rArO"]))

#ejercicio 11
print()
def add_item(list, item_to_add):
    new_list = list[:]
    new_list.append(item_to_add)
    return new_list

print(add_item([1,2,3,4,5], 6))

#ejercicio 12
print()
def remove_item(list,item_remove):
    new_list = list[:]
    try:
        new_list.remove(item_remove)
        return new_list
    except ValueError:
        return "dont found elemnt"

print(remove_item([1,2,3,4,5],4))

#ejercicio 13
print()
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(sum_of_numbers(100))

#ejercicio 14
print()
def sum_of_odds(n):
    total = 0
    for i in range(n+1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(5))

#ejercicio 15
print()
def sum_of_even(n):
    total = 0
    for i in range(n+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(5))
