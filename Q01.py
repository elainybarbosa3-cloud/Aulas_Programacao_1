tempo_horas = int(input("Digite a quantidades de horas: "))
tempo_minutos = int(input("Digite a quantidades de minutos: "))
tempo_segundos = (tempo_horas * 3600) + (tempo_minutos * 60)
print(f"Quantidade de segundos é: {tempo_segundos}s")