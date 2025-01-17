def encontrar_maior(n1, n2):
    if n1 >= n2: # alterei aqui
        return n1
    else:
        return n2
# A lógica estáa correta, mas tem um pequeno problema... Se n1=n2, não vai retornar nada

#muito bom
def main():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    maior_numero = encontrar_maior(num1, num2)
    print("O maior número é:", maior_numero)
main()

# corrigido
