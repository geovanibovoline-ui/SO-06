#Declarar
Num1: float = 0.0
Num2: float = 0.0

#Inicio
def calcular():
    global Num1, Num2
    if Num1 > Num2:
        print(Num1,"é maior do que", Num2)
    else:
        print(Num2,"é maior do que", Num1)
    #Fim-se
def main():
    global Num1, Num2
    Num1 = float(input("Digite o primeiro número real: "))
    Num2 = float(input("Digite o segundo número real: "))
    calcular()
main()
#Fim