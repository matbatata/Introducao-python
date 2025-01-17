def fatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return #Não é possível calcular o fatorial de um número negativo
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 2
        return result
def main():
    numero = int(input("Digite um número inteiro positivo: "))
    print("O fatorial de", numero, "é:", fatorial(numero))
main()

#explicar
