def imprimir_mes(numero):
    if numero == 1:
        print("Janeiro")
    elif numero == 2:
        print("Fevereiro")
    elif numero == 3:
        print("Março")
    elif numero == 4:
        print("Abril")
    elif numero == 5:
        print("Maio")
    elif numero == 6:
        print("Junho")
    elif numero == 7:
        print("Julho")
    elif numero == 8:
        print("Agosto")
    elif numero == 9:
        print("Setembro")
    elif numero == 10:
        print("Outubro")
    elif numero == 11:
        print("Novembro")
    elif numero == 12:
        print("Dezembro")
    else:
        print("Número inválido. Por favor, insira um número entre 1 e 12.")

def main():
    n = int(input("Digite um número de 1 a 12: "))
    imprimir_mes(n)

main()
# corrigido
