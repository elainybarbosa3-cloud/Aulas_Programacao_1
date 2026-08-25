try:
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    resultado = n1/n2
    print(f"O resultado da divisão é {resultado}")
except ValueError:
    print(f"Favor digitar somente números")
except ZeroDivisionError:
    print(f"Não é possível dividir um número por 0 ")
except Exception as erro:
      print("Ocorreu um erro: {erro}")
else:
    print("O programa foi executado corretamente")
finally:
      print("Programa finalizado")
    