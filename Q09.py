L1 = float(input("Digite o lado L1: "))
L2 = float(input("Digite o lado L2: "))
L3 = float(input("Digite o lado L3: "))

if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    print("Os valores formam um triângulo.")

    if L1 == L2 and L2 == L3:
        print("O triângulo é equilátero.")
    elif L1 != L2 and L1 != L3 and L2 != L3:
        print("O triângulo é escaleno.")
else:
    print("Os valores não formam um triângulo.")