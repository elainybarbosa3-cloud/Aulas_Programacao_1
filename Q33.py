tempo1 = float(input("Digite o tempo do servidor 1: "))
tempo2 = float(input("Digite o tempo do servidor 2: "))
tempo3 = float(input("Digite o tempo do servidor 3: "))
tempo4 = float(input("Digite o tempo do servidor 4: "))

menor = tempo1
servidor = 1

if tempo2 < menor:
    menor = tempo2
    servidor = 2

if tempo3 < menor:
    menor = tempo3
    servidor = 3

if tempo4 < menor:
    menor = tempo4
    servidor = 4

print(f"O servidor com menor tempo de resposta foi o servidor {servidor}.")
print(f"Tempo de resposta: {menor} ms")