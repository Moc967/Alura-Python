import forca
import advinhacao
print("****************************************")
print("***** Bem vindo a central de jogos *****")
print("****************************************")

print("\nEscolha o seu jogo:\n")
nivel = int(input("\t1 - Forca\n\t2 - Advinhação\n\t3 - Sair\n"))

if nivel == 1:
    print("********* Você escolheu jogar Forca ***********\n")
    forca.jogar()
elif nivel == 2:
    print("********* Você escolheu jogar Advinhação ***********\n")
    advinhacao.jogar()
elif nivel == 3:
    print("********* Até a próxima! ***********")
