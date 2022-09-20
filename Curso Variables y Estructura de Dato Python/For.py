# TALLER 5 PYTHON
# AUTOR: HAROLD VARGAS
# FECHA: 19/09/2022

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)
print()
print("Taller 5 ciclos iterativos con la sentencia FOR")
print()
num1=int(input("Digite primer número: "))
num2=int(input("Digite segundo número (mayor): "))
print("Ciclo para el primer número")

for i in range (num1):
    print(i)
print("Fin del ciclo")
print()

print("Ciclo desde el primer número hasta el segundo número")
for i in range (num1,num2):
    print(i)
print("Fin del ciclo")
print()

print("Ciclo desde el primer número hasta el segundo número con incrementos de 2")
for i in range (num1,num2,2):
    print(i)
print("Fin del ciclo")
print()

empresa=str(input("Digite el nombre de una empresa: "))
empresa= empresa.lower()
for character in empresa:
    print(character)
print("Fin del ciclo")
print()
print("Fin")
