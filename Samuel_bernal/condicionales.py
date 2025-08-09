#Ejercicio 1 Verficar si eres mayor de edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad")

#Ejercicio 2 Verficar si un numero es positivo o negativo
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("El número es positivo.")
else:
    print("El número es cero o negativo.")

#Ejercicio 3 Verficar si un numero es par o impar
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#Ejercicio 4  para ver el resultado de un puntaje de 0 a 100 
puntaje = int(input("Ingrese su puntaje: "))
if puntaje >= 90:
    print("Excelente")
elif puntaje >= 80:
    print("Muy bien")
elif puntaje >= 70:
    print("Bien")
elif puntaje >= 60:
    print("Raspado")
else:
    print("Estudie mas")   

#Ejercicio 5 para verificar si esta una fruta 
fruta = input("Ingrese el nombre de una fruta: ").lower()
if fruta == "manzana":
    print("La fruta manzana si se encuentra")
elif fruta == "banano":
    print("La fruta banano si se encuentra") 
elif fruta == "naranja":
    print("La fruta naranja si se encuentra")
elif fruta == "fresa":
    print("La fruta fresa si se encuentra")
else: 
    print("Fruta no encontrada")