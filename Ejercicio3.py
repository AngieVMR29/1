print("Bienvendido al programa")
personas=int(input("Ingrese la cantidad de personas "))
peso1=0
j=0
k=0
for i in range (personas):
    peso=int(input("Ingrese el peso"))
    edad=int(input("Ingrese la edad "))
    if (edad>=0 and edad<=12):
        k+=1
        peso1=peso1+peso
    elif(edad>=13 and edad<=29):
        categoria="Jovenes"
        j+=1
    elif (edad>30 and edad<=59):
        categoria="Adultos"

promedio=peso1/k
   