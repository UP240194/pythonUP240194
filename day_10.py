#nivel 10 parte 1

#ejercicio 1 
x = 0
print("\nIterating from 0 to 10 using for loop:")
for i in range(11): 
    print(i)

print("\nIterating from 0 to 10 using while loop:")
while x <= 10:  
    print(x)
    x += 1

#ejercicio 2
x = 10
print("\nIterating from 10 to 0 using for loop:")
for i in range(10, -1, -1): 

print("\nIterating from 10 to 0 using while loop:")
while x >= 0: 
    print(x)
    x -= 1

#ejercicio 3
x = 1
print()
while x <= 7: 
    print(x*"#")
    x += 1

#ejerciico 4
x = 0
print()
while x < 8:
    print("# " * 8)
    x+= 1

#ejercicio 5
x = 0
y = 0
print()
while x <=10:                   
    print(f"{x} x {y} = {x*y}") 
    x += 1
    y += 1

#ejercicio 6 
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']  
print()
for element in lista:   
    print(element)   

#ejercicio 7
x = 0
print()
while x <= 100:         
    if x % 2 == 0:      
        print(x)        
    x += 1

#ejercicio 8 
x = 0
print()
while x <= 100:        
    if x % 2 != 0:      
    x += 1