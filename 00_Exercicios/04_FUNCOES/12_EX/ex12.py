def maior_fator_primo(numero):
    fator = 2
    while fator * fator <= numero:
        if numero % fator == 0:
            numero //= fator
        else:
            fator += 1
    return numero
def main():
    numero = int(input("Insira um número inteiro positivo: "))
    resultado = maior_fator_primo(numero)
    print("O maior fator primo de", numero, "é:", resultado)
main()

#explicar
