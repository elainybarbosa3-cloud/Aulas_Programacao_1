preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade comprada: "))
desconto = float(input("Digite o desconto em reais: "))

total = (preco * quantidade) - desconto

print(f"Valor a pagar: R$ {total:.2f}")