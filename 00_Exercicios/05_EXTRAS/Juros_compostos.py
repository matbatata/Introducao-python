c = float(input("Capital: "))
i = float(input("Taxa (ex: 0.05): "))
t = float(input("Tempo: "))

m = c * (1 + i) ** t 

print(f"Montante: R$ {m:.2f}")