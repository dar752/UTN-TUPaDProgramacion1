1)
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

2)
nota = int(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

3)
numero = int(input("Por favor, ingrese un número: "))
if numero % 2 == 0:
    print("Su número es par")
else:
    print("Su número es impar")

4)
edad = int(input("Por favor, digite su edad: "))
if edad >= 0 and edad < 12:
    print("Usted es un niño")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto joven")
elif edad >= 30:
    print("Usted es un adulto")
else:
    print("Edad no valida")

5)
contraseña = input("Por favor, ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

6)
import random
import statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print("numerosaleatorios:", numeros_aleatorios)
print(f"media: {media:.2f}")
print(f"mediana: {mediana}")
print(f"moda: {moda}")

if media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No cumple con ninguno de los criterios necesarios")

7)
texto = input("Por favor, ingrese una palabra o frase: ")

if texto [-1].lower() in "aeiou":
    convocal = texto + "!"
    print(convocal)
else:
    print(texto)

8)
nombre = input("Por favor, ingrese su primer nombre: ")
print("Escriba 1 si quiere su nombre en mayúsculas")
print("Escriba 2 si quiere su nombre en minúsculas")
print("Escriba 3 si quiere la primera letra de su nombre en mayúscula")
opcion = (input("Escriba el número: "))
if opcion == "1":
    final = nombre.upper()
elif opcion == "2":
    final = nombre.lower()
elif opcion == "3":
    final = nombre.title()
else:
    final = "Opción no valida"

print(final)

9)
magnitud = int(input("Por favor, ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

10)
hemisferio = input("¿En que hemisferio se encuentra? (S/N): ")
mes = int(input("Ingrese el mes actual (1-12): " ))
dia = int(input("Ingrese el dia actual (1-31): " ))

if hemisferio == "S" or hemisferio == "s":
    if (mes == 12 and dia >= 21) or (mes <= 3 and mes != 3) or (mes == 3 and dia < 21):
        print("La estación es verano")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and mes != 6) or (mes == 6 and dia < 21):
        print("La estación es otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and mes != 9) or (mes == 9 and dia < 21):
        print("La estación es invierno")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and mes != 12) or (mes == 12 and dia < 21):
        print("La estación es primavera")
    else:
        print("Fechas invalidas")
        
if hemisferio == "N" or hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes <= 3 and mes != 3) or (mes == 3 and dia < 21):
        print("La estación es invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and mes != 6) or (mes == 6 and dia < 21):
        print("La estación es primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and mes != 9) or (mes == 9 and dia < 21):
        print("La estación es verano")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and mes != 12) or (mes == 12 and dia < 21):
        print("La estación es otoño")
    else:
        print("Fechas invalidas")