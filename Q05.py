numero = int(input("Digite o último número da placa: "))

if numero % 2 == 0:
    print("O número é par.")
    print("Utilize o Portão A.")
else:
    print("O número é ímpar.")
    print("Utilize o Portão B.")