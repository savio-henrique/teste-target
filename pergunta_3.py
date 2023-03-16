import json
import math

# Utilizando a biblioteca json para ler o arquivo e
# utilizando a biblioteca math para fazer contas aritméticas em digitos
# do tipo float sem a perca de precisão

def calculaMedia(vetor):
    numeros, media, dias_uteis = [], 0, 0
    for i in vetor:
        dias_uteis += 1
        numeros.append(i['valor'])

    # Calcular a média com math.fsum() para não perder a precisão matemática
    media = math.fsum(numeros)/dias_uteis

    return float(f"{media:.4f}")

def faturamento(vetor):
    maior = 0
    menor = 99999999999999999

    for i in vetor:
        # Se o valor for maior que o já maior valor, ele se tornará o novo maior valor
        if i['valor'] > maior:
            dia_maior = i['dia']
            maior = i['valor']

        # Se o valor for menor que o já menor valor, ele se tornará o novo menor valor
        if i['valor'] < menor:
            dia_menor = i['dia']
            menor = i['valor']

    return dia_menor, menor, dia_maior, maior

def quantosDias(vetor):
    qtd_dias = 0

    media = calculaMedia(vetor)

    for i in vetor:
        if i['valor'] > media:
            qtd_dias += 1
    return qtd_dias

def main():
    arquivo = json.loads(open("./dados/dados.json").read())
    # List compreehension para retirar os dias sem faturamento
    arquivo = [i for i in arquivo if i['valor'] != 0.0]

    dias = quantosDias(arquivo)
    dia_menor, menor, dia_maior, maior = faturamento(arquivo)

    # Imprime a sequência de informações pedidas pela questão
    print(f"O menor valor de faturamento do mês ocorreu no dia {dia_menor} e foi de R${menor}.")
    print(f"O maior valor de faturamento do mês ocorreu no dia {dia_maior} e foi de R${maior}.")
    print(f"A quantidade de dias em que o valor de faturamento diário foi maior que a média do mês foram: {dias} dias.")

main()