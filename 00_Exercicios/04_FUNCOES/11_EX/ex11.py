def calcular_potencia(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * calcular_potencia(x, y - 1)
def main():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    resultado = calcular_potencia(x, y)
    print("O resultado de", x, "elevado a", y, "é igual a", resultado)
main()

#Explicar
