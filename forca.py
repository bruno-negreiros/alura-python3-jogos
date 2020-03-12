import random

def jogar():

    arquivo = open("frutas.txt", "r")
    frutas = []
    for linha in arquivo:
        frutas.append(arquivo.readline().strip())
    palavra_secreta = frutas[random.randrange(0, len(frutas))].upper()
    arquivo.close()

    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    tentativas_maximas = 6

    print("\n")    
    print(33 * "x")
    print("Bem vindo ao jogo de Forca!")
    print(33 * "x")

    while (not enforcou and not acertou):
        print()
        print(letras_acertadas)
        chute = input("Informe uma letra: ")
        chute = chute.strip().upper()

        index = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = chute
                index = index + 1
        
        else:
            erros += 1
            if (erros != 6):
                print("Você errou!")
                print("Você ainda possui {} tentativas.".format(tentativas_maximas-erros))

        enforcou = erros == tentativas_maximas
        acertou = "_" not in letras_acertadas

        if(acertou):
            print()
            print(letras_acertadas)

    print("Fim de jogo!")
    
    if (enforcou):
        print("Você Perdeu!")
        print("Palavra secreta = {}".format(palavra_secreta))
        print()
    else:
        print("Você Ganhou!")
        print()

if (__name__ == "__main__"):
    jogar()