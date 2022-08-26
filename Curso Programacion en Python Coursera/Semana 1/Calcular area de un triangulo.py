s1 = int(input("Ingrese Valor de lado 1: "))
s2 = int(input("Ingrese Valor de lado 2: "))
s3 = int(input("Ingrese Valor de lado 3: "))

def area_triangulo (s1:int,s2:int,s3:int)->int:
    s = (s1+s2+s3)/2
    area=((s*(s-s1)*(s-s2)*(s-s3))**0.5)
    return round (area,2) 

