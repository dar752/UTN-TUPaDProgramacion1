1)
for i in range(101):
    print(i)

2)
num = int(input("Por favor, digite un numero entero: "))
digitos = len(str(abs(num)))

print(f"El numero ingrsado tiene {digitos} digitos")

3)
primero = int(input("Por favor, digite el primer numero: "))
segundo = int(input("Por favor, digite el segundo numero: "))

if primero > segundo:
    primero, segundo = segundo, primero

suma = 0
for i in range(primero + 1, segundo):
    suma += i

print("La suma de todos los digitos entre los dos numeros dados es de:", suma)

4)
suma = 0
numero = 1
while numero != 0:
    numero = int(input("Por favor, ingrese un numero entero (0 para detener la suma): "))
    print(numero)
    suma += numero
print("El total de la suma de los numeros:", suma)

5)
import random
numero_escondido = random.randint(0, 9)
num = int(input("ingrese un numero del 0 al 9: "))
intentos = 1
while num != numero_escondido:
    num = int(input("Ingrese otro numero: "))
    intentos += 1
print(f"Felicidades! el numero era {numero_escondido}, intentos:", intentos)

6)
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

7)
num = int(input("Por favor, ingrese un numero entero positivo: "))
if num > 0:
    num = round(num)
    suma = 0
    for i in range(0, num + 1, 1):
        suma += i
    print(f"La suma de los numeros entre 0 y {num}:", suma)
else:
    print("Debe ser un numero positivo")


8)
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(1, 101, 1):
    num = int(input("Por favor, ingrese un digito: "))
    if num % 2 == 0:
        pares = pares + 1
    elif num % 2 != 0:
        impares = impares + 1
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1

print("Pares:", pares)
print("impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)


9)
suma = 0
for i in range(1, 11, 1):
    digito = int(input("Por favor, ingrese un digito: "))
    suma += digito

print("La media de los numeros ingresados es de:", suma / 10)


10)
num = (input("Por favor, digite un numero: "))
invertido = num [::-1]
print("Su numero invertido es:", invertido)
