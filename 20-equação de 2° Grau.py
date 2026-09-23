#Declarar
A: float = 0.0
B: float = 0.0
C: float = 0.0
raiz1: float = 0.0
raiz2: float = 0.0

#Inicio
def calcular():
    global A,B,C,raiz1,raiz2
    delta: float = (B ** 2) - (4 * A * C)
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz: float = -B / (2 * A)
        print("A equação possui uma raiz real:", raiz)
    else:
        raiz1 = (-B + (delta ** 0.5)) / (2 * A)
        raiz2 = (-B - (delta ** 0.5)) / (2 * A)
    print("A equação possui duas raízes reais:", raiz1, "e", raiz2)
    #Fim-se
def main():
    global A,B,C
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))
    calcular()
main()
#Fim