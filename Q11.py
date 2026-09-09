emprestimo = float(input("Digite o valor emprestado: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite a quantidade de meses: "))

juros = emprestimo * (taxa / 100) * meses
montante = emprestimo + juros

print(f"Juros pagos: R$ {juros:.2f}")
print(f"Montante total: R$ {montante:.2f}")