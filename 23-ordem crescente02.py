#Declarar (obrigatório em ordem crescente)
Num1: float = 0.0
Num2: float = 0.0
Num3: float = 0.0
#Declarar (em qualquer ordem)
Num4: float = 0.0

#Inicio
def calcular():
    global Num1,Num2,Num3,Num4
    numeros = [Num1, Num2, Num3, Num4]
    numeros_ordenados = sorted(numeros)
    print("Números em ordem crescente:", numeros_ordenados)
def main():
    global Num1,Num2,Num3,Num4
    Num1 = float(input("Digite o primeiro número (em ordem crescente): "))
    Num2 = float(input("Digite o segundo número (em ordem crescente): "))
    Num3 = float(input("Digite o terceiro número (em ordem crescente): "))
    Num4 = float(input("Digite o quarto número (fora da ordem): "))
    calcular()
main()
#Fim