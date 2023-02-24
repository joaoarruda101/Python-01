import array as arr
historico = []

def adicionar_historico(operacao, num1, num2, resultado):
    historico.append(f"{num1} {operacao} {num2} = {resultado}")

def mostrar_historico():
    for operacao in historico:
        print(operacao)

def calculadora():
  while True:
    operacao = input("Digite a operação desejada (+, -, *, /) ou 'sair' para encerrar: ")
    if operacao == "sair":
        break
    num1 = float(input("Dígite o primeiro número: "))
    num2 = float(input("Dígite o segundo número"))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 + num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação Inválida!")
        continue

    adicionar_historico(operacao, num1, num2, resultado)
    print("O Resultado é: ", resultado)

    mostrar_historico()

    array = arr.array('i', [int(resultado)])
    print(array[0])

calculadora()



