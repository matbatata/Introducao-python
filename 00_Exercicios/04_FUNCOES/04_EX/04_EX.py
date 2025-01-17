def calcular_volume_cilindro(altura, raio):
    pi = 3.1414592
    v = pi * (raio ** 2) * altura
    return round(v, 2)  

def main():    
    altura = float(input("Insira a altura (em m): "))
    raio = float(input("Insira o raio (em m): "))
    v = calcular_volume_cilindro(altura, raio)
    print("O volume do cilindro é:", v)


main()
#corrigido
