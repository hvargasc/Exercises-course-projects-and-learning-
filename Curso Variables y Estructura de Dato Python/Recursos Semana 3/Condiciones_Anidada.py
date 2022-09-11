# TALLER 4 PYTHON
# AUTOR: HAROLD VARGAS
# FECHA: 10/09/2022

from datetime import date
hoy = date.today() # Fecha Actual
print("Hoy es el día: ", hoy)
print()
print("Ejercicio de las clases de triangulos")
a=int(input("Ingrese el primer lado: "))
b=int(input("Ingrese el segundo lado: "))
c=int(input("Ingrese el tercer lado: "))

if a==b and a==c and b==c:
    print("El triangulo es un Triangulo Equilatero")
else:
    if a==b or b==c or a==c:
        print("El triangulo es un triangulo Isoceles")
    else:
        print("El triangulo es un triangulo Escaleno")
print()

animal=str(input("Digite un animal: "))
animal=animal.upper()
if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre ", animal) 
elif animal == "GATO":
    print("Este animal persigue a los ratones ", animal)
elif animal == "OSO":
    print("Este animal vive en el polo norte ", animal) 
else:
    print("Este animal no es PERRO, GATO ni OSO... es: ", animal)
print()
print("FIN")    