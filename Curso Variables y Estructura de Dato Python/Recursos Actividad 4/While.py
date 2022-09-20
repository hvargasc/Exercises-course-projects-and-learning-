# TALLER 6 PYTHON
# AUTOR: HAROLD VARGAS
# FECHA: 19/09/2022

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)
print()
print("Taller 6 ciclos iterativos con la sentencia While")
print()

num1=int(input("Digite un numero: "))
print("***Ciclo controlado por contador")
i=1
while i<= num1:
    print(i)
    i+=1
print("Fin del ciclo")
print()

print("***Ciclo controlado por evento")
i=1
numero1=5
numero2=int(input("Digite un numero de 1 a 10: "))
while numero2 != numero1:
    i+=1
    numero2 = int(input("Digite un numero de 1 a 10: "))
print("Acertaste en el intento No. ", i)
print("Fin del ciclo")
print()

print("***Ciclo abortado con la sentencia break")
amistad=input("Digite el nombre de un amigo: ")
amistad = amistad.upper()
for character in amistad:
    print(character)
    if character =="A":
        break
print("fin del ciclo")
print()
print("FIN")