import random

print("***************************************")
print("*** Bem vindo ao jogo de Advinhação ***")
print("***************************************")

numeroSecreto = random.randrange(1, 60)
cont = 5

while cont > 0:
    cont = cont - 1
    chute = int(input("Escolha um número entre 1 e 60 \n"))
    if chute == numeroSecreto:
        print("Parabens!! Voce acertou o número secreto")
        break
    else:
        if cont == 0:
            print("Voce realizou todas as tentativas e não acertou o número secreto.")
        else:
            print("Voce não acertou. Tente novamente")

