def generar_n_primos(N): #Función generar n numeros primos 
     primos  = [] # lista primos 
     valor = 2  # valor inicial
     while len(primos) < N: # bucle 
         prueba_primo = [valor for i in primos if valor%i == 0] # operación para evaluar si el numero iterado es primo 
         primos += [] if prueba_primo else [valor] # aumenta y almacena en la lista primos si la prueba_primo es True, sino aumenta el numero de valor 
         valor += 1 # aumentar el valor inicial 
     return primos # devuelve la lista primos 

# Mensaje del programa 
print("---------------------------------")
print("numeros primos")
print("---------------------------------")

n = int(input("Ingrese a cantidad de numeros primos  que quiere obtener: "))# Cantidad de numeros primos n que el usuario quiere conocer

if(n <= 0): # conidicional para evaluar si el valor ingresado por el usuario es correcto 
    print("Número no es válido") # Mensaje de error en el número ingresado
else:
    print (generar_n_primos(n)) # Imprime la lista con los números primos para n numeros 
