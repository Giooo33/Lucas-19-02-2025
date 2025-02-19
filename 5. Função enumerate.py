#5. Função Enumerate

#Utilize enumerate para exibir os elementos da lista ['Python', 'Java', 'C++', 'JavaScript'] 
# acompanhados de seus índices.

lista = ['Python', 'Java', 'C++', 'JavaScript'] 

for indice, palavra in enumerate(lista):

    print(f"{indice}: {palavra}")

#Dada a lista [100, 200, 300, 400], exiba os elementos cujo índice seja
#par.

lista = [100, 200, 300, 400]
pares = []

for indice, elemento in enumerate(lista):

    if indice % 2 == 0:
        pares.append(elemento)

print(f"{indice}")