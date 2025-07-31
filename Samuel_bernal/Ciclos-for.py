#Ejercicio 1  imprimir Numeros del 1 al 20 
for i in range(1, 21):
    print(i)

#Ejercicio 2 Una suma de Numeros  de una lista 
numeros = [100, 200, 300, 400, 500]
suma = 0
for numero in numeros:
    suma += numero
print("La suma de los números es:", suma)

#Ejercicio 3 tabla de multiplicar del 5
numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Ejercicio 4 contar vocales en una palabra
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1
print("El numero de vocales en tu palabra es: ", contador_vocales)

#Ejercio 5 para sacar los numeros pares del 1 al 50 
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
        
