# titulol del programa

print("--------------------------------------------------------")
print("Programa para solucionar la ecuación de segundo grado:")
print("--------------------------------------------------------")

#declaracion de variables 

num_a = 3 # variable a
print("la variable a es :" + str(num_a))
num_b = -5 # variable b
print("la variable b es :" + str(num_b))
num_c = 1 # variable c
print("la variable c es :" + str(num_c) + "\n")

num1 = -(num_b) # -b
num2 = (num_b)**2 # variable b elevada al cuadrado 
num3 = (4 * num_a * num_c) # 4 * a * c que va dentro de la fórmula para resolver la ecuación
num4 = pow((num2-num3),0.5) # solución de la raíz cuadrada de la fórmula para resolver la ecuación
num5 = num1+num4 # Suma de los resultantes de la ecuación
num6 = num5/(2*num_a) # División del resultado por 2*a
print("El resultado de la Ecuación por determinante positivo de la ecuación con variables a, b y c es: \n")
print(str(num6) + "\n") # Resultado de la ecuacion con las variables a, b y c 

