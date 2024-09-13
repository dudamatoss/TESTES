def inverter(s):

    resultado =''  

    for char in s:
        resultado = char + resultado
    return resultado



palavra = input("Digite a string que deseja inverter: ")
inverter = inverter(palavra)

print(f"String original: {palavra}")
print(f"String invertida: {inverter}")