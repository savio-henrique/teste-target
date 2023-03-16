import math

# Uso da biblioteca math para cálculos precisos com dados do tipo float

def main():
    faturamento = {"SP":67836.43,
                   "RJ":36678.66,
                   "MG":29229.88,
                   "ES":27165.48,
                   "Outros":19849.53}

    # Calcula o valor total do faturamento mensal
    total = round(math.fsum(faturamento.values()),2)

    porcentagem = {}
    for estado in faturamento:
        # Grava a porcentagem do valor de cada estado em relação ao valor total
        porcentagem[estado] = faturamento[estado] / total

    # Imprime o estado e sua porcentagem
    for estado in porcentagem:
        print(f"O faturamento de {estado} representa aproximadamente {porcentagem[estado]*100:.2f}% do valor total mensal.")

main()