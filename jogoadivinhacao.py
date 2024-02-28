print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o numero secreto
numeroSecreto = 16

#Definindo o numero tentativas
numerotentativas = 3

while(numerotentativas>0):
     print('ok')

#Recebendo o chute do jogador
    chuteString=input('Digite um número: ')
    print('Você digitou o número: ',chuteString)
    chute=int(chuteString)

#Declaracao as condições
    if numeroSecreto == chute:
        print('Você acertou!')
    elif(chute>numeroSecreto):
        print('Voce errou!! O número secreto é numero menor')
    else:
        print('Você errou!! O numero secreto é um número maior')