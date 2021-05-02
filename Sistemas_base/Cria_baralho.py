
def cria_baralho():

    baralho = []

    #cartas = 0

    numeros = ['A' ,2,3,4,5,6,7,8,9,10,'J', 'Q', 'K']

    #while cartas != 52:
        
    for espadas in numeros :

        baralho.append('{0}♠'.format(espadas))

    for copas in numeros:

        baralho.append('{0}♥'.format(copas))

    for ouros in numeros:

        baralho.append('{0}♦'.format(ouros))

    for paus in numeros:

        baralho.append('{0}♣'.format(paus))

    return baralho