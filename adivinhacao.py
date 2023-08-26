import random

def jogar():

    print("*********************************")
    print("Bem-Vindo ao jogo da adivinhacao!")
    print("*********************************")

    numero_secreto = round(random.randrange(0,100))
    tentativas = 3
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Facil \n(2) Medio \n(3) Dificil")

    nivel = int(input("Defina um nivel:"))

    if(nivel == 1):
        tentativas = 15
    elif(nivel == 2):
        tentativas = 7
    elif(nivel ==3):
        tentativas = 3
    else:
        print("Digite uma das opcoes validas!")
        exit()

    for rodada in range (1, tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, tentativas))
        chute_str = input("Digite seu numero entre 1 e 100:")
        print("Voce digitou:",chute_str)
        chute   = int(chute_str)

        if(chute < 1 and chute > 100):
            print("Voce deve digitar um numero de 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!" .format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! Chutou acima do valor...")
            elif(menor):
                print("Voce errou! Chutou abaixo do valor...")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("Fim do jogo.")
        
if(__name__ == "__main__"):
    jogar()