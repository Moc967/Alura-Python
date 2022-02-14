import random


def jogar():
    print("****************************************")
    print("****** Bem vindo ao jogo de Forca ******")
    print("****************************************")
    print("\nVocê terá até seis chances para acertar \na palavra secreta.\n\n\tBoa sorte!!\n")
    print("****************************************")

    arquivo = open("arquivo.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    indice = random.randrange(0, len(palavras))

    palavra_secreta = palavras[indice].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas, "\n")

    while not enforcou and not acertou:

        chute = input("escolha uma letra\n")
        chute = chute.strip().upper()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index]= letra
                # print("Encontrei a letra {} na posicao {}".format(chute, index))
            index += 1
        else:
            erros += 1
        enforcou = erros == 8
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("Parabens!!! Voce acertou a palavra secreta:", palavra_secreta)
    else:
        print("Voce perdeu!!")

if __name__ == "__main__":
    jogar()
