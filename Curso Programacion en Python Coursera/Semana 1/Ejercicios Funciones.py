x1 = int(input("Ingrese el valor de X1: "))
x2 = int(input("Ingrese el valor de X2: "))
x3 = int(input("Ingrese el valor de X3: ")) 

temporal = x1

x1 = x3
x3 = x2
x2 = temporal
print (str(x1)+", "+str(x2)+", "+str(x3))
