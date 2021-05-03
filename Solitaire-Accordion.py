import random
from Sistemas_base.Cria_baralho import *
from Sistemas_base.Empilha_carta import *
from Sistemas_base.Extrai_naipe import *
from Sistemas_base.Extrai_valor import *
from Sistemas_base.Jogadas_possíveis import *
from Sistemas_base.possui_movimentos import *

print("Bem vindo ao Paciência Acordeão! 🇧🇷\nWelcome to Solitaire Accordion! 🇺🇸\n==================================")

def Jogar():
    pilha = []
    baralho = cria_baralho()
    random.shuffle(baralho)
    pilha = baralho
    while True:
        if len(pilha) == 1:
            print("VOCÊ VENCEU O JOGO! (YOU WON!)")
            break
        if not possui_movimentos_possiveis(pilha):
            print("VOCÊ PERDEU O JOGO! (YOU LOST!)")
            break
        print("Estado atual do baralho: (Current state of the deck: )")
        for i in range(len(baralho)):
            print(str(i+1) + ": " + baralho[i])
        alvo = input("Escolha uma carta para trocar (Choose a card) [2-{}]".format(len(pilha)))
        if not alvo.isdigit() or (alvo.isdigit() and int(alvo) <= 1) or (alvo.isdigit() and int(alvo) > len(pilha)):
            print("Input inválido! Escolha um número entre 2 e {} (Invalid Input)".format(len(pilha)))
        else:
            pass

def Denovo():
    denovo = input("\nJogar de novo?(Play again?) (Y/N)")
    if denovo == "N" or denovo == "n":
        exit()

while True:
    Jogar()
    Denovo()