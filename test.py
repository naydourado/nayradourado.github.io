def main():
    # Solicitar a entrada do usuário
    numeros = input("Digite uma lista de números inteiros separados por espaço: ")
    
    # Converter a entrada para uma lista de inteiros
    numeros = list(map(int, numeros.split()))
    
    # Inicializar contadores
    pares = 0
    impares = 0
    
    # Contar números pares e ímpares
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    # Retornar os resultados como uma tupla
    return (pares, impares)

# Executar a função e imprimir o resultado
resultado = main()
print(f"Quantidade de números pares: {resultado[0]}")
print(f"Quantidade de números ímpares: {resultado[1]}")
