#Declarar
Num1: int = 0
Num2: int = 0

#Inicio
def calcular():
    global Num2,Num1
    if Num1 > Num2:
        print(Num1, "é maior que", Num2)
    else:
        print(Num2, "é maior que", Num1)
    #Fim-se
def main():
    global Num1,Num2
    Num1 = int(input("Digite o primeiro número: "))
    Num2 = int(input("Digite o segundo número: "))
    calcular()
main()
#Fim