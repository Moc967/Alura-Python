import random

print("***************************************")
print("*** Bem vindo ao jogo de Advinhação ***")
print("***************************************")
print("\nVocê terá cinco chances de acertar o número sorteado.\nBoa sorte!!\n")

rodada = 1
max_range = 0
total_de_tentativas = 0

print("Selecione o grau de dificuldade desejado:\n")
print("1 - Baixo\n2 - Médio\n3 - Alto")
nivel = int(input("Qual a sua opção?\n"))

if nivel == 1:
    max_range = 20
    total_de_tentativas = 7
elif nivel == 2:
    max_range = 40
    total_de_tentativas = 6
elif nivel == 3:
    max_range = 60
    total_de_tentativas = 5

numero_secreto = random.randrange(1, max_range)

while rodada <= total_de_tentativas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # print("Tentativa {1} de {0}".format(rodada, total_de_tentativas))
    msg_entrada = "Escolha um número entre 1 e " + str(max_range)+"\n"

    chute = input(msg_entrada)
    chute2 = int(chute)
    rodada = rodada + 1
    if chute2 < 1 or chute2 > max_range:
        print(chute, "está fora da faixa permitida\n")
        rodada = rodada - 1
        continue
    if chute2 > numero_secreto:
        print("O número informado é maior que o número secreto")
    elif chute2 < numero_secreto:
        print("O número informado é menor que o número secreto")
    else:
        print("Parabens!! Voce acertou o número secreto")
        break
    if rodada == 6:
        print("\nVoce realizou todas as tentativas e não acertou o número secreto.")
    else:
        print("Tente novamente\n")
