import math

opcao = int(input("Escolha uma opção (1 - Hipotenusa / 2 - Cateto): "))

if opcao == 1:
    cateto1 = float(input("Digite o primeiro cateto: "))
    cateto2 = float(input("Digite o segundo cateto: "))

    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

    print("Hipotenusa:", hipotenusa)

elif opcao == 2:
    hipotenusa = float(input("Digite a hipotenusa: "))
    cateto = float(input("Digite o outro cateto: "))

    resultado = math.sqrt(hipotenusa ** 2 - cateto ** 2)

    print("Cateto:", resultado)

else:
    print("Opção inválida.")