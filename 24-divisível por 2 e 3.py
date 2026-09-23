#Declarar
Num: int = 0

#Inicio
def calcular():
    global Num
    if Num % 2 == 0 and Num % 3 == 0:
        print("O número é divisível por 2 e 3")
    else:
        print("O número não é divisível por 2 e 3")
    #Fim-se
def main():
    global Num
    Num = int(input("Digite um número: "))
    calcular()
main()
#Fim