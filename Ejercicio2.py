print("Bienvenid@")
superficie=int(input("Ingrese los metros cuadrados de la superficie "))
if(superficie>1000000):
    pino=superficie*70/100
    oyamel=superficie*20/100
    cedro = superficie*10/100
    print(f"Para pino debe sembra 70% que es: {pino}")
    print(f"Para oyamel debe sembrar 20% que es: {oyamel}")
    print(f"Para cedro debe sembrar 10% que es: {cedro}")
elif(superficie<=1000000):
    pino=superficie*50/100
    oyamel=superficie*30/100
    cedro=superficie*20/100
    print(f"Para pino debe sembrar 50% que es: {pino}")
    print(f"Para oyamel debe sembrar 30% que es: {oyamel}")
    print(f"Para cedro debe sembrar 20% que es: {cedro}")
    