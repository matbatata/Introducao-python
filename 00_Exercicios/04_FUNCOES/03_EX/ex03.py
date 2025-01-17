def fahrenheit_para_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32.0) * (5.0/9.0)
    return temp_celsius

def main():
    temperatura_fahrenheit = float(input("Insira a temperatura em graus Fahrenheit: "))
    temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
    print("A temperatura em Celsius é:", temperatura_celsius)

main()
#corrigido 
