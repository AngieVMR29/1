print("Bienvenid@ al programa que calcula el salario semanal de los obreros")
obreros=int(input("Ingrese el número de obreros "))
for i in range(obreros):
    horas=int(input(f"Ingrese las horas trabajadas del obrero {i+1}: "))

    if(horas<=40):
        salario=20*horas
        print(f"Su salario semanal es {salario}")
    elif(horas>40):
        horasT=40
        salario=40*20
        horaex=horas-40
        extra=horaex*25
        print(f"Su salario semanal es {salario} y el extra es: {extra}")
