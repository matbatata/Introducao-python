def imc(peso, altura):
    return round(peso / (altura * altura), 2)

def main():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    print(imc(peso, altura))

main()

#corrigido
