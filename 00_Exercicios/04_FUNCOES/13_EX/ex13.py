def calcular_somatorio(n):
    somatorio = n * (n + 1) // 2
    return somatorio
def main():
    n = int(input("Digite um número inteiro positivo: "))
    resultado = calcular_somatorio(n)
    print("O somatório de 1 até", n, "é igual a", resultado)
main()

#explicar
