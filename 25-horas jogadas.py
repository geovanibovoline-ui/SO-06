#Declarar
hora_inicio = 0
minuto_inicio = 0
hora_final = 0
minuto_final = 0
tempo = 0
horas = 0
minutos = 0

#Inicio
def calcular():
    global hora_inicio, minuto_inicio
    global hora_final, minuto_final
    global tempo, horas, minutos
    inicio = hora_inicio * 60 + minuto_inicio
    final = hora_final * 60 + minuto_final
    if final < inicio:
        final = final + 24 * 60
    #Fim-se
    tempo = final - inicio
    horas = tempo // 60
    minutos = tempo % 60
    print("Tempo de jogo:", horas, "horas e", minutos, "minutos")
def main():
    global hora_inicio, minuto_inicio
    global hora_final, minuto_final
    hora_inicio = int(input("Digite a hora de início: "))
    minuto_inicio = int(input("Digite os minutos de início: "))
    hora_final = int(input("Digite a hora de término: "))
    minuto_final = int(input("Digite os minutos de término: "))
    calcular()
main()
#Fim