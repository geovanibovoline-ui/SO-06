#Declarar
nota_bimestre1: float = 0.0
nota_bimestre2: float = 0.0
nota_bimestre3: float = 0.0
nota_bimestre4: float = 0.0

#Inicio
def calcular():
    global nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4
    media: float = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4) / 4
    if media >= 6.0:
        print("Aprovado! Média:", media)    
    elif media < 6.0 and media >= 3.0:
        print("Exame para recuperação!", "Média:", media)
    else:
        print("Reprovado! Média:", media)
        #Fim-se
def main():
    global nota_bimestre4,nota_bimestre3,nota_bimestre2,nota_bimestre1
    nota_bimestre1 = float(input("Digite a nota do 1º bimestre: "))
    nota_bimestre2 = float(input("Digite a nota do 2º bimestre: "))
    nota_bimestre3 = float(input("Digite a nota do 3º bimestre: "))
    nota_bimestre4 = float(input("Digite a nota do 4º bimestre: "))
    calcular()
main()
#Fim