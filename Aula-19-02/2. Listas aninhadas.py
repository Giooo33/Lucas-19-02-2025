#2. Listas aninhadas

#Crie uma matriz 3x3 utilizando listas aninhadas e exiba seus elementos em formato de tabela.

matriz = [
    ["a", 1, 2],
    [3, "b", 4],
    [5, 6, "c"]
]

for matriz in matriz:
    print(matriz)

#Dada a matriz abaixo, substitua o elemento central por 0 e exiba a matriz atualizada:
#matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
          ]

matriz[1][1] = 0

for matriz in matriz:

    print(matriz)
