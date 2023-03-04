from brzcode import *

numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha1= aleatorizarLista(numeros)
escolha2= aleatorizarLista(numeros)

resposta= perguntar('inteiro', f'Quanto é {escolha1}x{escolha2}?')
se(resposta,'==',escolha1*escolha2,cor('verde') + 'Acertou!', cor('vermelho') + f'Você errou! O resultado é {escolha1*escolha2}')
