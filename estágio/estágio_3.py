import json

def faturamento_diario(caminho_arquivo):
    with open(caminho_arquivo, 'r') as faturamento:
        dados = json.load(faturamento)

    faturamento_valido = []
    for dado in dados['faturamento']:
        if dado['valor'] > 0:
            faturamento_valido.append(dado['valor'])
    
    # Verifica se a lista de faturamento válido não está vazia
    if not faturamento_valido:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_da_media": 0
        }

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)
    acima_media = sum(1 for valor in faturamento_valido if valor > media_faturamento)

    return {
        "menor_valor": menor_faturamento,
        "maior_valor": maior_faturamento,
        "dias_acima_da_media": acima_media
    }


caminho_arquivo = '3.json'
resultado = faturamento_diario(caminho_arquivo)

print("----------------------------------------")
print(f"Menor valor de faturamento: {resultado['menor_valor']:.2f}")
print(f"Maior valor de faturamento: {resultado['maior_valor']:.2f}")
print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_da_media']}")
print("---------------------------------------")

