
def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

#print(empilha(['6♥', 'J♥', '9♣', '9♥'],1,0))