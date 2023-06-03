print("Bienvenid@")
inverT=int(input("Ingrese la inversión total: "))
hipot=int(input("Ingrese el monto de la hipoteca: "))
faltante=inverT-hipot
if(hipot<1000000):
    inverT=inverT*50/100
    print(f"Usted debe invertir {inverT} y el socio debe invertir {inverT}")
elif(hipot>=1000000):
    faltante=faltante*50/100
    print(f"Usted debe inviertir {inverT+faltante}\n El restante del socio es {faltante}")

