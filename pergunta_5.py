def main():
    frase = input()

    # Utilizando a ferramenta de slice do python ->
    # print(frase[-1::-1])

    reverse = ''
    for i in range(len(frase)):
        # Multipliqua o index por -1 para começar do
        # último índice da frase em diante, invertendo o resultado
        temp = frase[(1+i)*(-1)]
        reverse += temp

    print(f"A string '{frase}' invertida é: '{reverse}'.")

main()