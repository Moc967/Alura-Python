import random

print("***************************************")
print("*** Bem vindo ao jogo de Advinhação ***")
print("***************************************")
print("\nVocê terá cinco chances de acertar o número sorteado.\nBoa sorte!!\n")

maxRange = 60
rodada = 1
totalDeTentativas = 5
numeroSecreto = random.randrange(1, maxRange)

while rodada <= totalDeTentativas:
    print("Tentativa {} de {}".format(rodada, totalDeTentativas))
    chute = int(input("Escolha um número entre 1 e 60 \n"))
    rodada = rodada + 1
    if chute > maxRange:
        print(chute, "está fora da faixa permitida\n")
        rodada = rodada - 1
    else:
        if chute > numeroSecreto:
            print("O número informado é maior que o número secreto")
        elif chute < numeroSecreto:
            print("O número informado é menor que o número secreto")
        else:
            print("Parabens!! Voce acertou o número secreto")
            break
        if rodada == 6:
            print("\nVoce realizou todas as tentativas e não acertou o número secreto.")
        else:
            print("Tente novamente\n")
