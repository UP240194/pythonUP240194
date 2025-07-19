#dia 12 nivel 1 

#ejerciico 1 
import random
def random_user_id():
    characters = "lalalaladhfcuwhfwe"
    user_id = ''.join(random.choice(characters) for i in range(6))
    return user_id

print(f"\n{random_user_id()}")

#ejercicio 2 
import random

def user_id_gen_by_user():
    try:
        num_characters = int(input("\nEnter the number of characters per ID: "))
        num_ids_to_generate = int(input("Enter the number of IDs to generate: "))
    except ValueError:
        print("\nInvalid input. Please enter whole numbers.")
        return
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for _ in range(num_ids_to_generate):
        user_id = "".join(random.choice(characters) for i in range(num_characters))
        print(user_id)

user_id_gen_by_user()

#ejercicio 3 
def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    rgb_string = f"\nrgb({red},{green},{blue})"
    return rgb_string

print(rgb_color_gen())