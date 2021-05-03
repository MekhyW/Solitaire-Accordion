import random
from Sistemas_base.Cria_baralho import *
from Sistemas_base.Empilha_carta import *
from Sistemas_base.Extrai_naipe import *
from Sistemas_base.Extrai_valor import *
from Sistemas_base.Jogadas_possíveis import *

print("Bem vindo ao Paciência Acordeão! 🇧🇷\nWelcome to Solitaire Accordion! 🇺🇸\n==================================")

def Jogar():
    baralho = cria_baralho()
    random.shuffle(baralho)
    pilha = [baralho[0], baralho[1], baralho[2], baralho[3]]
    print(pilha)

def Denovo():
    denovo = input("\nJogar de novo?(Play again?) (Y/N)")
    if denovo == "N" or denovo == "n":
        exit()

while True:
    Jogar()
    Denovo()