
def extrai_naipe(carta):

    carta = str(carta)
    for t in carta:

        if t == '♦' or t =='♥' or t == '♣' or t == '♠':

            return t