valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = valor1 + valor2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = valor1 - valor2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = valor1 * valor2
    print("Resultado:", resultado)

elif operacao == "/":
    if valor2 != 0:
        resultado = valor1 / valor2
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Operação inválida.")