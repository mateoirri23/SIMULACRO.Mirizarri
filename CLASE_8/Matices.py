matriz_4X4 = [
    [1, 2, 3, 4 ],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

def recorrer_matriz(matriz):    #------->Desempaqueta la matriz
    for i in range(len(matriz_4X4)):
        for j in range(len(matriz_4X4[i])):
            print(f"Elemento en la posición ({i}, {j}): {matriz_4X4[i][j]}", end = "")
            