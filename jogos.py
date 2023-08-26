import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo*******!")
    print("*********************************")

    print("(1) Jogo da Forca \n(2) Jogo da Adivinhacao")
    jogo = int(input("Selecio o jogo:"))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()
    else:
        print("Selecione uma opcao valida!")
        exit()

if(__name__ == "__main__"):
    escolher_jogo()