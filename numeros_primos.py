

print("---------------------------------")
print("numeros primos\n")

numero = int(input("Ingrese a cantidad de numeros primos  que quiere obtener: "))

def primo(numero):
 if numero < 2:  # si es menor de 2 no es primo, devolverá Falso
   return False
 for i in range(2, numero):  # un ciclo desde el 2 hasta el num de entrada
   if numero % i == 0:  # si el resto da 0 no es primo, devuelve Falso
    return False
 return True  # de lo contrario devuelve Verdadero
 print(primo(3))

if (numero <= 0):
    print("número no es valido")
else:
    pass



