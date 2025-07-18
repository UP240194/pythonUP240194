#nivel 2 dia 10

#ejericico 1 
x = 0
suma = 0
print()
while x <= 100:
    suma += x   
    x += 1
print(f"the sum of all numbers of 0 to 100 is {suma}")

#ejercicio 2 
x = 0
suma_par = 0
suma_impar = 0
print()
while x <= 100:             
    if x % 2 == 0:         
        suma_par += x       
    else:
        suma_impar += x     
    
    x += 1
print(f"the sum of all evens numbers of 0 to 100 is {suma_par}")        
print(f"the sum of all odds numbers of 0 to 100 is {suma_impar}")


