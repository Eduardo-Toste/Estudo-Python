print("*********************************")
print("Bem-Vindo ao jogo da adivinhacao!")
print("*********************************")

numero_secreto = 42
rodada = 1
tentativas = 3

while (rodada <= tentativas):
    print("Tentativa {} de {}" .format(rodada, tentativas))
    chute_str = input("Digite seu numero:")
    print("Voce digitou:",chute_str)
    chute   = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou!")
    else:
        if(maior):
            print("Voce errou! Chutou acima do valor...")
        elif(menor):
            print("Voce errou! Chutou abaixo do valor...")

    rodada += 1
    print("Fim do jogo.")