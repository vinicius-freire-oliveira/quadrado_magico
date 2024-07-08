# Quadrado mágico - Combinações que somadas resultam em 15
# Definição da função para gerar combinações de três números cuja soma seja 15
def gera_combinacoes(lista, n):    
    # Loop sobre todos os elementos da lista
    for i in lista:
        for j in lista:            
            # Verifica se a soma dos três números é igual a 15
            # e se os números são diferentes uns dos outros
            if n + i + j == 15 and (n != i and n != j and i != j):
                # Adiciona a combinação à lista de combinações
                combinacoes.append((n, i, j))

# Definição da função para gerar um quadrado mágico
def gera_quadro(comb, L1):
    # Define a primeira linha do quadrado mágico como a linha fornecida
    linha1 = L1    
    # Loop sobre todas as combinações possíveis para as linhas 2 e 3
    for i in range(len(comb)):
        linha2 = comb[i]
        for j in range(len(comb)):
            linha3 = comb[j]            
            # Verifica se a soma das linhas, colunas e diagonais é igual a 15
            if (linha1[0] + linha2[0] + linha3[0] == 15) and\
               (linha1[1] + linha2[1] + linha3[1] == 15) and\
               (linha1[2] + linha2[2] + linha3[2] == 15) and\
               (linha1[0] + linha2[1] + linha3[2] == 15) and\
               (linha1[2] + linha2[1] + linha3[0] == 15):     
                # Verifica se a primeira linha não tem nenhum número em comum com a segunda linha
                if (linha1[0] not in linha2) and\
                   (linha1[1] not in linha2) and\
                   (linha1[2] not in linha2):
                    # Se todas as condições forem satisfeitas, imprime o quadrado mágico
                    print(linha1)
                    print(linha2)
                    print(linha3)
                    print()

# Lista de números de 1 a 9
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Lista para armazenar as combinações de três números cuja soma é 15
combinacoes = []

# Loop para gerar as combinações de três números para cada número de 1 a 9
for n in range(1,10):    
    gera_combinacoes(lista, n)

print()

# Loop para tentar formar quadrados mágicos com base nas combinações geradas
for L1 in combinacoes:
    gera_quadro(combinacoes, L1)