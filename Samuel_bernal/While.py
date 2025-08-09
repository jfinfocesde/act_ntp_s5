#Ejercicio 1 para hacer un bucle cuando el contador sea menor que 10 
contador = 0  
while contador < 10:
    print(f"El contador es: {contador}") 
    contador += 1 

#Ejercicio 2 para contraseña correcta 
contrasena_correcta = "cesde123"
contrasena_ingresada = ""
while contrasena_ingresada != contrasena_correcta:
    contrasena_ingresada = input("Ingresa la contraseña: ")
    if contrasena_ingresada != contrasena_correcta:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
print("¡Acceso concedido!")

#Ejercicio 3 para sumar números hasta que se ingrese un 0
suma = 0    
numero = None
while numero != 0:
    numero = int(input("Ingresa un número ( y cuando desees terminar ingrese 0 ): "))
    suma += numero
print(f"La suma de los números ingresados es: {suma}")

#Ejercicio 4 para validar un usuario 
nombre = ""

while len(nombre) < 2:
    nombre = input("Por favor, ingresa tu usuario solo letras y minimo 2: ")

print(f"Hola, {nombre}. ¡Bienvenido!")

#Ejercio 5 un menu de comidas
opcion = ''

while opcion != '3':
    print("\n   Menú de Comidas   ")
    print("1.Comidas:")
    print("2. Bebidas:")
    print("3. Salir")
    opcion = input("Escoja la Opcion que desee: ")

    if opcion == '1':
        print(" Pizza,Sopa,Ensalada, Hamburguesa, Tacos, Sushi")
    elif opcion == '2':
        print(" Agua, Jugo, Gasimba, Tinto, Guarito, Ronsito")
    elif opcion == '3':
        print("Hasta luego")
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
