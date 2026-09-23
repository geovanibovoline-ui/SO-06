#Declarar
Num1: int = 0
Num2: int = 0

#Inicio
def calcular():
    global Num1,Num2
    if Num1 > Num2 and Num1 % Num2 == 0:
        print(f"{Num1} é múltiplo de {Num2}")
    elif Num2 > Num1 and Num2 % Num1 == 0:
        print(f"{Num2} é múltiplo de {Num1}")
    else:
        print(f"Nenhum dos números é múltiplo do outro")
    #Fim-se
def main():
    global Num1,Num2
    Num1 = int(input("Digite o primeiro número: "))
    Num2 = int(input("Digite o segundo número: "))
    calcular()
main()
#Fim