
capital = float(input("Ingrese capital inicial: "))
tasa = float(input("Ingrese tasa anual: "))
tiempo = int(input("Ingrese número de años: "))

valor_futuro = capital * (1 + (tasa/100))**tiempo

print ("Valor futuro del tiempo inicial $"+str(valor_futuro)+", transcurridos "+str(tiempo)+" años y a una tasa del "+str(tasa))