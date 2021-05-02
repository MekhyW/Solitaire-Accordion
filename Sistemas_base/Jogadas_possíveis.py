
def extrai_naipe(carta):

    carta = str(carta)
    for t in carta:

        if t == '♦' or t =='♥' or t == '♣' or t == '♠':

            return t
def extrai_valor(carta):

    carta = str(carta)
    
    if '10' in carta:

        return '10'

    else:

        return carta[0]
def lista_movimentos_possiveis(baralho,indice):    
    jogadas = []    
    if indice == 0:
        return jogadas       
    naipe = extrai_naipe(baralho[indice])
    naipe_anterior = extrai_naipe(baralho[indice - 1])
    if indice >= 3:        
        naipe_terceiro = extrai_naipe(baralho[indice - 3])
    valor = extrai_valor(baralho[indice])
    valor_anterior = extrai_valor(baralho[indice - 1])    
    if indice >= 3:
        valor_terceiro = extrai_valor(baralho[indice - 3])
    if naipe == naipe_anterior or valor == valor_anterior:
        jogadas.append(1)
    if indice >= 3:
        if naipe == naipe_terceiro or valor == valor_terceiro:
            jogadas.append(3)    
    return jogadas

#print(lista_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥'],1))


        