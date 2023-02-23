print("*********************************")
print("Bem vindo no jogo de adivinhação")
print("*********************************")

numero_secreto = 42
chute_str = input("Digite o seu número: ")
print("Você digitou" , chute_str)

chute = int(chute_str)

if(chute_str == numero_secreto):
   print("Você acertou")
else:
   print("Você errou")

print("FIM DO JOGO");

