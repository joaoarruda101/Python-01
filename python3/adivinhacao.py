print("*********************************")
print("Bem vindo no jogo de adivinhação")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

while(total_de_tentativas > 0):
   chute_str = input("Digite o seu número: ")
   print("Você digitou" , chute_str)

   chute = int(chute_str)
   acertou = chute == numero_secreto
   maior = chute > numero_secreto
   menor = chute < numero_secreto
   
   if(acertou):
      print("Você acertou")
   else:
      if(maior):
       print("Você errou! O seu chute foi *MAIOR* que o número secreto!")
      elif(menor):
         print("Você errou! o seu chute foi *MENOR* do que o número secreto!")
   print("FIM DO JOGO");
   
   idade1 = 10;
   idade2 = int("20");
   print(idade1 + idade2)



