peso_lb=float(180)
altura_inch=float()

altura = altura_inch/30.48
peso = peso_lb* 0.45

print ("Su peso en kg es: "+str(peso))

def calcular_BMI (altura:float,peso:float)->float:
    BMI = peso/(altura^2)
    return round(BMI,2)

