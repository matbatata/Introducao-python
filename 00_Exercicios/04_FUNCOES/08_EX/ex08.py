def eh_quadrado_perfeito(numero):
    return int(numero ** 0.5) ** 2 == numero #ok
    
def main():
    exemplos = [1, 4, 9, 10, 16, 25] # não aprendemos isso
    for num in exemplos: # não aprendemos
        if eh_quadrado_perfeito(num):
            print(num, "é um quadrado perfeito.")#ok
        else:
            print(num, "não é um quadrado perfeito.") #ok
main() 

 
# explicar
