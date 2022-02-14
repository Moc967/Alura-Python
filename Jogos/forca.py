import random

def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas, "\n")

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 8
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        game_over(palavra_secreta)

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabens!!!\nVoce acertou a palavra secreta:", palavra_secreta)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def game_over(palavra_secreta):
    print("@@@@@ Game Over @@@@")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            # print("Encontrei a letra {} na posicao {}".format(chute, index))
        index += 1

def pede_chute():
    chute = input("escolha uma letra\n")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_de_abertura():
    print("**********************************")
    print("*** Bem vindo ao jogo de Forca ***")
    print("**********************************")
    print(" Você terá até seis chances para  "
          "\n\tacertar a palavra secreta.\n\n\t\tBoa sorte!!")
    print("**********************************")

def carrega_palavra_secreta():
    arquivo = open("arquivo.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if __name__ == "__main__":
    jogar()