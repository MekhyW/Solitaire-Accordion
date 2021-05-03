from Extrai_naipe import *
from Extrai_valor import *
from Jogadas_possíveis import *  
#----------A parte de cima ja faz parte dos outos códigos-----------
def possui_movimentos_possiveis(baralho):
    t = 0
    tem = 0    
    while t != len(baralho):
        #print(t)
        if lista_movimentos_possiveis(baralho,t) == []:
            t += 1            
        else:
            tem += 1
            t += 1
    if tem == 0:
        return False
    else:        
         return True
#print(possui_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥']))



