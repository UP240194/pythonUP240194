#dia 12 nivel 2 

#ejercicio 1 
print()
def list_of_hexa_colors(n_colors = 1):
    hex_characters = "0123456789abcdef"
    generated_colors = []
    for _ in range(n_colors):
        hex_code = "#"
        for _ in range(6):
            hex_code += random.choice(hex_characters)
        generated_colors.append(hex_code)
    return generated_colors

print(list_of_hexa_colors())

#ejerciico 2 
print()
def list_of_rgb_colors(n_colors = 1):
    generated_colors = []
    for _ in range(n_colors):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        rgb_stri = f"rgb({red},{green},{blue})"
        generated_colors.append(rgb_stri)
    return generated_colors

print(list_of_rgb_colors())

#ejercicio 3 
def generate_colors(color_type, n_colors):
    generated_list = []
    if color_type == "hexa":
        for _ in range(n_colors):
            generated_list.append(list_of_hexa_colors())
    elif color_type == "rgb":
        for _ in range(n_colors):
            generated_list.append(list_of_rgb_colors())
    return generated_list

print()
print(generate_colors("hexa",2))