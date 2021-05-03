import os
import random
from Sistemas_base.Cria_baralho import *
from Sistemas_base.Empilha_carta import *
from Sistemas_base.Extrai_naipe import *
from Sistemas_base.Extrai_valor import *
from Sistemas_base.Jogadas_possíveis import *
from Sistemas_base.possui_movimentos import *

print("Bem vindo ao Paciência Acordeão! 🇧🇷\nWelcome to Solitaire Accordion! 🇺🇸\n==================================")
print("\nRegras (Rules): https://www.youtube.com/watch?v=gLUxTvT59Qg (video from the youtuber EverythingMom)")
input("Aperte [Enter] para começar a jogar (Press [Enter] to begin)")
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\nIniciando primeiro jogo... (starting first game...)\n")

def ImprimeEstadoAtual(baralho):
    print("Estado atual do baralho: (Current state of the deck: )")
    for i in range(len(baralho)):
        print(str(i+1) + ": " + baralho[i])

def Jogar():
    pilha = []
    baralho = cria_baralho()
    random.shuffle(baralho)
    pilha = baralho
    ImprimeEstadoAtual(pilha)
    while True:
        if len(pilha) == 1:
            print("VOCÊ VENCEU O JOGO! (YOU WON!)")
            break
        if not possui_movimentos_possiveis(pilha):
            print("VOCÊ PERDEU O JOGO! (YOU LOST!)")
            break
        alvo = input("Escolha uma carta para mover (Choose a card) [2-{}]".format(len(pilha)))
        if not alvo.isdigit() or (alvo.isdigit() and int(alvo) <= 1) or (alvo.isdigit() and int(alvo) > len(pilha)):
            print("Input inválido! Escolha um número entre 2 e {} (Invalid Input)".format(len(pilha)))
        elif lista_movimentos_possiveis(pilha, int(alvo)-1) == []:
            print("Não é possível mover essa carta! Escolha outra carta (You must choose a different card)")
        else:
            while True:
                alvo2 = input("Escolha a carta sobre a qual você quer empilhar a primeira (Choose second card)")
                if int(alvo2) not in lista_movimentos_possiveis(pilha, int(alvo)-1):
                    print("Segunda carta inválida! Escolha outro movimento (Invalid second card)")
                    print(lista_movimentos_possiveis(pilha, int(alvo)-1))
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    empilha(pilha, int(alvo)-1, int(alvo2)-1)
                    ImprimeEstadoAtual(pilha)
                    break

def Denovo():
    denovo = input("\nJogar de novo?(Play again?) (Y/N)")
    if denovo == "N" or denovo == "n":
        exit()

while True:
    Jogar()
    Denovo()