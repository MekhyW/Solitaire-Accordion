from Sistemas_base.Cria_baralho import *
from Sistemas_base.Empilha_carta import *
from Sistemas_base.Extrai_naipe import *
from Sistemas_base.Extrai_valor import *
from Sistemas_base.Jogadas_possíveis import *

def Jogar():
    pass

def Denovo():
    denovo = input("Jogar novamente? (S/N)")
    if denovo == "N" or denovo == "n":
        exit()

while True:
    Jogar()
    Denovo()