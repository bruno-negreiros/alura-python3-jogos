def jogar():

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    print("\n")    
    print(33 * "x")
    print("Bem vindo ao jogo de Forca!")
    print(33 * "x")
    print()
    print(letras_acertadas)
    print()

    while (not enforcou and not acertou):
        chute = input("Informe uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = chute.upper()
            index = index + 1
        print(letras_acertadas)
        print()
    
    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()