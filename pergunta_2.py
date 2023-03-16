def fibWhile(num_informado):
    # Casos base quando fib(0) = 0 e fib(1) = 1
    calculados = [0,1]

    # Enquanto o último número calculado da sequência de Fibonnaci for menor
    # que o número informado, ele calcula o próximo número da sequência
    while calculados[-1] < num_informado:
        calculados.append(calculados[-1]+calculados[-2])

    # Se o número está na sequência
    if num_informado in calculados:
        return f"O número {num_informado} pertence à sequência de Fibonacci"
    else:
        return f"O número {num_informado} não pertence à sequência de Fibonacci"

def main():
    #Recebe o número que se deseja verificar
    numero = int(input())
    # Imprime o resultado
    print(fibWhile(numero))

main()