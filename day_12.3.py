#dia 12 nivel 3

#ejercicio 1 
import random

def shuffle_list(list):
    shuffled_copy = list[:]
    random.shuffle(shuffled_copy)
    return shuffled_copy

print()
print(shuffle_list([1,2,3,4,5]))


#ejercicio 2
print()
def generate_unique_seven_numbers():
    population = list(range(10))
    unique_nums = random.sample(population, 7)
    return unique_nums

print(generate_unique_seven_numbers())