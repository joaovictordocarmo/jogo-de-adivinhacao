import forca
import jogoadivinhacao
print("**************")
print("*******Escolha o seu jogo!*******")
print("**********************")

print("(1)Forca(2)Adivinhacao")

jogo = int(input("qual jogo?"))

#criando a condicao
if(jogo ==1):
    print("jogando jogo Forca")
    forca.jogar_forca()
else:
    print("jogando jogo da adivinhacao") 
    jogoadivinhacao.jogar_adivinhacao()
