def converter_para_segundos(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos
    
def main():
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    total_segundos = converter_para_segundos(horas, minutos, segundos)
    print("O total de segundos é:", total_segundos)
main()

#corrigido
