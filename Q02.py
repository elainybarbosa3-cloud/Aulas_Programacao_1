tempo_horas = int(input("informe a hora: "))
tempo_segundos = tempo_horas *3600
distancia_quilometros = 30 * tempo_segundos
distancia_metros = distancia_quilometros * 1000
print(f"distancia percorrida em metros: {distancia_metros}m/s")