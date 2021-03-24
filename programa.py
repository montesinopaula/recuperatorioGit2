"""
#Calcula el mayor entre dos números.
#lee dos números
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))

#Determina el número más grande
if numero1> numero2:
    maximo = numero1
else:
    maximo = numero2

#Imprimir el resultado
print("El máximo es: ", maximo)
#---------------------------------------------------------#
#Calculo el máximo entre tres números
#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande

maximo = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > maximo:
    maximo = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > maximo:
    maximo = numero3



print("El máximo número es:", maximo)

#------------------------------------------------#
#Determina el largo de un lista 
lista =  input("Ingresa una lista: ")  
   

totalElementos = 0

for i in lista:
    totalElementos += 1

print("El número de elementos de la lista", totalElementos)

#---------------------------------------------#
# Determina si es vocal o consomante.
letra=input("ingrese una letra: ")
letra=letra.lower() 
if letra == "a" or letra == "e"  or letra == "i"  or letra == "o" or letra == "u":
    print("es vocal")
else: 
    print("es consonante")
"""
#----------------------------------------------#
# Suma los elementos de una lista.

def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])

print(sumalista([1,3,5,7,9]))

#------------------------------------------------#
# Multiplica los elementos de una lista.
def multilista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] * multilista(listaNumeros[1:])

print(multilista([1,1,2]))




  
