# TALLER 2 PYTHON
# AUTOR: HAROLD VARGAS
# FECHA: 03/09/2022

from datetime import date
hoy = date.today()      #Fecha actual
print ("Hoy es el día: ", hoy)

a= int(input("Digite primer número: "))
b= int(input("Digite segundo número: "))
c= int(input("Digite tercer número: "))
x= [a,b,c]
print("El valor maximo es: ", max(x))
print("El valor minimo es: ", min(x))
print("La suma de los 3 número es: ", sum(x))
print()
z=float(input("Digite un número con decimales; "))
redondo=round(z)
print ("El valor de ",z,"redondeado es: ", redondo)
print ()
frase=str(input("Digite una frase: "))
print("La frase en mayusculas es: ", frase.upper())
print("La frase en minusculas es: ", frase.lower())
print("La frase con mayusculas inicial es: ", frase.capitalize())
print("La frase con palabras en mayusculas es:", frase.title())
print("La logitud de la frase es;", len(frase), "caracteres")
print()
print("FIN")
