def jogar():
    print("*********************************")
    print("***Bem-Vindo ao jogo da forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Escolha uma letra:")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posicao {}!" .format(letra,posicao))
            posicao = posicao + 1
            
        print("Jogando...")

    print("Fim do jogo.")
    
if(__name__ == "__main__"):
    jogar()