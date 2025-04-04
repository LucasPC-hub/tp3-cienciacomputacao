import multiprocessing as mp
import numpy as np
import time


def multiplicar_linha(linha_a, matriz_b):
    resultado = []
    for j in range(len(matriz_b[0])):
        soma = 0
        for k in range(len(matriz_b)):
            soma += linha_a[k] * matriz_b[k][j]
        resultado.append(soma)
    return resultado


def multiplicar_matrizes_paralelo(matriz_a, matriz_b):
    linhas_a = len(matriz_a)
    pool = mp.Pool(processes=linhas_a)

    resultados = [pool.apply_async(multiplicar_linha, args=(matriz_a[i], matriz_b))
                  for i in range(linhas_a)]

    matriz_resultado = [res.get() for res in resultados]

    pool.close()
    pool.join()

    return matriz_resultado


def multiplicar_matrizes_sequencial(matriz_a, matriz_b):
    linhas_a = len(matriz_a)
    colunas_b = len(matriz_b[0])
    matriz_resultado = []

    for i in range(linhas_a):
        linha_resultado = []
        for j in range(colunas_b):
            soma = 0
            for k in range(len(matriz_b)):
                soma += matriz_a[i][k] * matriz_b[k][j]
            linha_resultado.append(soma)
        matriz_resultado.append(linha_resultado)

    return matriz_resultado


def imprimir_matriz(matriz, nome):
    print(f"\n{nome}:")
    for linha in matriz:
        print(" ".join(f"{valor:4}" for valor in linha))


if __name__ == "__main__":
    matriz_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matriz_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    print("Multiplicação de Matrizes 3x3")
    imprimir_matriz(matriz_a, "Matriz A")
    imprimir_matriz(matriz_b, "Matriz B")

    inicio = time.time()
    resultado_sequencial = multiplicar_matrizes_sequencial(matriz_a, matriz_b)
    tempo_sequencial = time.time() - inicio

    inicio = time.time()
    resultado_paralelo = multiplicar_matrizes_paralelo(matriz_a, matriz_b)
    tempo_paralelo = time.time() - inicio

    imprimir_matriz(resultado_paralelo, "Resultado (Paralelo)")

    print(f"\nTempo sequencial: {tempo_sequencial:.6f} segundos")
    print(f"Tempo paralelo: {tempo_paralelo:.6f} segundos")
    print(f"Speedup: {tempo_sequencial / tempo_paralelo:.2f}x")

    resultados_iguais = np.array_equal(np.array(resultado_sequencial),
                                       np.array(resultado_paralelo))
    print(f"Resultados iguais: {resultados_iguais}")