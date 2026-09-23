#Declarar
Num1: int = 0
Num2: int = 0
diferenca: int = 0

#Inicio
def calcular():
    global Num1, Num2, diferenca
    if Num1 > Num2:
        diferenca = Num1 - Num2
    else:
        diferenca = Num2 - Num1
    #Fim-se
    print("A diferença entre os dois números é:",diferenca)
def main():
    global Num1, Num2
    Num1 = int(input("Digite o primeiro número inteiro: "))
    Num2 = int(input("Digite o segundo número inteiro: "))
    calcular()
main()
#Fim