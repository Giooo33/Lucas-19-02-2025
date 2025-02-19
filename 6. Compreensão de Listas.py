#6. Compreensão de Listas

#Crie uma lista com os quadrados dos números de 1 a 10 usando
# compreensão de listas.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = []

for numero in numeros:

    quadrado.append(numero **2)
    
print(quadrado)

#Filtre apenas os números pares da lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# utilizando compreensão de listas.

lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares= []

for verifica in lista:

    if verifica % 2 == 0:
        pares.append(verifica)

print(pares)
