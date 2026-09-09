nome = input("Digite o nome do participante: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano_nascimento

if idade >= 18:
    situacao = "Pode entrar desacompanhado."
else:
    situacao = "Precisa estar acompanhado por um responsável."

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Situação: {situacao}")