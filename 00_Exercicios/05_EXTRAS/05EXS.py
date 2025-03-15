x = int(input("Digite um número: "))
potencia = 0

while potencia <= 5:
    # Calcula o dígito atual
    digito = (x // pow(10, potencia)) % 10
    print(digito)
    potencia += 1
print("Potência final:", potencia)
