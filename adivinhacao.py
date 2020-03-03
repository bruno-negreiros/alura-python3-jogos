import random

def jogar():

    print("\n")
    print(33 * "x")
    print("Bem vindo ao jogo de Adivinhação!")
    print(33 * "x")

    numero_secreto = random.randrange(1, 101)
    dificuldade = 0
    pontos = 1000

    while (dificuldade != 1 and dificuldade != 2 and dificuldade != 3):
        print()
        print("Níveis de Jogo")
        print("[1] - Fácil")
        print("[2] - Médio")
        print("[3] - Difícil")
        dificuldade = int(input("Informe o nível de Dificuldade: "))

        if (dificuldade != 1 and dificuldade != 2 and dificuldade != 3):
            print("Valor Inválido!")

    if (dificuldade == 1):
        numero_de_tentativas = 20
    elif  (dificuldade == 2):
        numero_de_tentativas = 10
    else: 
        numero_de_tentativas = 5

    for rodada in range (1, numero_de_tentativas + 1):

        print()
        chute = int(input("Rodada {} de {} - Qual é o número secreto? ".format(rodada, numero_de_tentativas)))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns, você acertou e fez {}!\n".format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior que o número secreto.")
            elif (menor):
                print("O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()