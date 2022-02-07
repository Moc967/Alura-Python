import random

print("***************************************")
print("*** Bem vindo ao jogo de Advinhação ***")
print("***************************************")
print("\nVocê terá cinco chances de acertar o número sorteado.\nBoa sorte!!\n")

maxrange = 60
cont = 5
numeroSecreto = random.randrange(1, maxrange)
while cont > 0:
    cont = cont - 1
    chute = int(input("Escolha um número entre 1 e 60 \n"))

    if chute > maxrange:
        print(chute, "está fora da faixa permitida\n")
        cont = cont + 1
    else:
        if chute > numeroSecreto:
            print("O número informado é maior que o número secreto")
        elif chute < numeroSecreto:
                print("O número informado é menor que o número secreto")
            else:
                print("Parabens!! Voce acertou o número secreto")
                break
        if cont == 0:
            print("Voce realizou todas as tentativas, e não acertou o número secreto.")
        else:
            print("Tente novamente\n")
