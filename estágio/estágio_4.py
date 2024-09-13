SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP +RJ + MG + ES + Outros
print(total)

percentual_SP = (SP / total) * 100
percentual_RJ = (RJ / total) * 100
percentual_MG = (MG / total) * 100
percentual_ES = (ES / total) * 100
percentual = (Outros / total) * 100


print("Percentual de representação por estado:")
print(f"SP: {percentual_SP:.2f}%")
print(f"RJ: {percentual_RJ:.2f}%")
print(f"MG: {percentual_MG:.2f}%")
print(f"ES: {percentual_ES:.2f}%")
print(f"Outros: {percentual:.2f}%")


