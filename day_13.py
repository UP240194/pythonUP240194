numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [n for n in numbers if n <= 0]
print(neg_and_zero)
# Output: [-4, -3, -2, -1, 0]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuple_list)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
transformed = [[country.upper(), country[:3].upper(), city.upper()] 
               for [[(country, city)]] in countries]
print(transformed)
# Output: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
dict_list = [{'country': country.upper(), 'city': city.upper()} 
             for [[(country, city)]] in countries]
print(dict_list)
# Output: [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[(first, last)]] in names]
print(full_names)
# Output: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda m, x, y: y - m * x
print(slope(1, 2, 3, 6))         # Output: 2.0
print(y_intercept(2, 1, 2))      # Output: 0.0