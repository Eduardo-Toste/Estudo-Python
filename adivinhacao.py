print("*********************************")
print("Bem-Vindo ao jogo da adivinhacao!")
print("*********************************")

numero_secreto = 42
rodada = 1
tentativas = 3

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
        print("Voce acertou!")
        break
    else:
        if(maior):
            print("Voce errou! Chutou acima do valor...")
        elif(menor):
            print("Voce errou! Chutou abaixo do valor...")

    print("Fim do jogo.")