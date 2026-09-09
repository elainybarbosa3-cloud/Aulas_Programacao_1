import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

print(f"Delta = {delta}")

if delta < 0:
    print("Não há raízes reais.")

elif delta == 0:
    x = -b / (2 * a)
    print(f"A única raiz real é: {x}")

else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"As duas raízes reais são: {x1} e {x2}")