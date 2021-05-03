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
    while not possui_movimentos_possiveis(pilha):
        baralho = cria_baralho()
        random.shuffle(baralho)
        pilha = [baralho[0], baralho[1], baralho[2], baralho[3]]
    while True:
        if len(pilha) == 1:
            print("VOCÊ VENCEU O JOGO! (YOU WON!)")
            break
        if not possui_movimentos_possiveis(pilha):
            print("VOCÊ PERDEU O JOGO! (YOU LOST!)")
            break

def Denovo():
    denovo = input("\nJogar de novo?(Play again?) (Y/N)")
    if denovo == "N" or denovo == "n":
        exit()

while True:
    Jogar()
    Denovo()