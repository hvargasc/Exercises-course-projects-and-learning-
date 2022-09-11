# TALLER 3 PYTHON
# AUTOR: HAROLD VARGAS
# FECHA: 10/09/2022

from datetime import date
from traceback import print_tb
hoy = date.today() # Fecha Actual
print("Hoy es el día: ", hoy)

a = int(input("Digite eel valor de A: "))
b = int(input("Digite eel valor de B: "))
if a>=b:
    print("A es mayor o igual que B")
else:
    print("A es menor que B")

print ()
curso = "Requerimientos"
curso2 = "Algoritmos"

print ("El curso1 es: ", curso)
print ("El curso2 es: ", curso2)

if curso=="Requerimientos" and curso2 == "Algoritmos":
    print("Usted estudia programación de software")
else:
    print("Usted estudia otro programa diferente a programación de Software")
print()
print("***   Final del Análisis del programa de Formación SENA   ***")
print()
frase=input("digite una oración: ")
print("La frase en mayusculas es: ", frase.upper())
longitud= len(frase)
print("La longitud de la frase es: ", longitud, " caracteres")
if longitud >10:
    print("La frase contiene mas de 10 caracteres")
else:
    print("La frase contiene menos de 11 caracteres")
print()
print("FIN")
