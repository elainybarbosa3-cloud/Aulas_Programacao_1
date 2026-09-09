soma = 0
quantidade = 0

for i in range(5):
    valor = float(input(f"Digite a {i + 1}ª medição: "))

    if valor > 0 and valor < 1000:
        soma += valor
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print("Média das medições válidas:", media)
else:
    print("Nenhuma medição válida foi informada.")