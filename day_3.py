#ejercicio 1
edad = 19
#ejercicio 2
altura = 1.64
#ejercicio 3
no_complejo=complex

#ejercicio 4
base = 20
altura = 10

area= (base*altura*0.5)
print('la base del triangulo es:',base,'la altura del triangulo es:',altura,'su area es de:',area)

#ejercicio 5
side_a= 5
side_b=4
side_c=3
perimetro=(side_a+side_b+side_c)
print(perimetro)

#ejercicio 6
length= float(input("introduzca la altura del rectangulo"))
width= float(input("introduca el ancho del rectanculo"))
area=(length*width)
perimetro=2*(length+width)
print(f"Area es igual a: {area}")
print(f"Perimetro es igual a: {perimetro}")

#ejercicio 7
radio=float(input("ingresa el radio del circulo"))
pi= 3.14
area = (pi * radio*radio)
circumference = 2 *( pi * radio)
print(f"Area es igual a: {area}")
print(f"Perimetro es igual a: {perimetro}")
print(f"la circunferencia es igua a: {circumference}")

#ejericio 8
pendiente = 2
y_intercept = -2
x_intercept = 1
print(f"Equation: y = 2x - 2")
print(f"Pendiente: {pendiente}")
print(f"Y-intercept: (0, {y_intercept})")
print(f"X-intercept: ({x_intercept}, 0)")

#ejercicio 9
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia =((x2 - x1)**2 + (y2 - y1)**2)
print(f"la pendiente entre los puntos es de: {pendiente}")
print(f"ditancia eclaudiana es de: {distancia}")

#ejercico 10
pendiente_eq = 2            
pendiente_punto = (10 - 2) / (6 - 2)
if pendiente_eq == pendiente_punto:
    print("las pendientes son iguales a.")
else:
    print("las pendientes son distintas")
print(f"pendiente en ec: {pendiente_eq}")
print(f"pendiente en punto: {pendiente_punto}")

#ejercicio 11
for x in range(-10, 6):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"y es cero cuando x = {x}")

#ejercicio 12
palabra1 = "python"
palabra2 = "dragon"
len1 = len(palabra1)
len2 = len(palabra2)
print(f"Longuitud de'{palabra1}': {len1}")
print(f"Longuitud de '{palabra2}': {len2}")
comparacion = len1 > len2
print(f"la palabra  '{palabra1}' es mejor '{palabra2}'? {comparacion}")

#ejercicio 13
palabra1 = "python"
palabra2 = "dragon"
resultado = 'en' in palabra1 and 'en' in palabra2
print(f"se encuentra 'en' '{palabra1}' y'{palabra2}'? {resultado}")

#ejercicio 14
oracion = "Espero que este curso no esté lleno de jerga."
if "jerga" in  oracion:
  print("La palabra 'jerga' está en la oración.")
else:
  print("La palabra 'jerga' no está en la oración.")

#ejercicio 15 
palabra1 = "dragon"
palabra2 = "python"
if "on" not in palabra1:
  print("No hay 'on' en 'dragon'.")
else:
  print("Hay 'on' en 'dragon'.")

if "on" not in palabra2:
  print("No hay 'on' en 'python'.")
else:
  print("Hay 'on' en 'python'.")

#ejecicio 16
texto = "python"
longitud = len(texto)
longitud_flotante = float(longitud)
longitud_cadena = str(longitud_flotante)
print(f"La longitud original es: {longitud}")
print(f"La longitud como flotante es: {longitud_flotante}")
print(f"La longitud como cadena es: '{longitud_cadena}'")

#ejercicio 17
numero = 10

if numero % 2 == 0:
  print(f"El número {numero} es par.")
else:
  print(f"El número {numero} es impar.")

numero_impar = 7

if numero_impar % 2 == 0:
  print(f"El número {numero_impar} es par.")
else:
  print(f"El número {numero_impar} es impar.")

#ejercicio 18
resultado_division_entera = 7 // 3
valor_convertido_entero = int(2.7)

if resultado_division_entera == valor_convertido_entero:
  print("La división entera de 7 por 3 es igual al valor entero convertido de 2.7.")
else:
  print("La división entera de 7 por 3 NO es igual al valor entero convertido de 2.7.")

#ejercicio 19
valor1 = '10'
valor2 = 10

if type(valor1) == type(valor2):
  print("Los tipos de '10' y 10 son iguales.")
else:
  print("Los tipos de '10' y 10 son diferentes.")

#ejercicio 20
int('9.8') == 10
int(float('9.8')) == 10  

#ejercicio 21
horas = float(input("Ingresa las horas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
pago = horas * tarifa
print(f"Tu ganancia semanal es {pago}")

#ejercicio 22
anios = int(input("Ingresa el número de años que has vivido: "))
segundos = anios * 365 * 24 * 60 * 60
print(f"Has vivido {segundos} segundos.")

#ejercicio 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
