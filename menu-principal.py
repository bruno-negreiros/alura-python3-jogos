import adivinhacao
import forca

print(33 * "x")
print("MENU PRINCIPAL")
print(33 * "x")

op = 0

while (op != 1 and op != 2):
    print("[1] - Adivinhacao")
    print("[2] - Forca")
    op = int(input("Escolha um jogo: "))

    if (op != 1 and op != 2):
        print("Opção Inválida!\n")

if (op == 1):
    adivinhacao.jogar()
else:
    forca.jogar()