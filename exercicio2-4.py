import multiprocessing as mp
import math
import time


def conta_primos_sequencial(inicio, fim):
    contador = 0
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            contador += 1
    return contador


def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def conta_primos_intervalo(inicio, fim):
    contador = 0
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            contador += 1
    return contador


def conta_primos_paralelo(inicio, fim):
    num_processos = mp.cpu_count()
    tamanho_intervalo = (fim - inicio + 1) // num_processos

    intervalo = []
    for i in range(num_processos):
        inicio_intervalo = inicio + i * tamanho_intervalo
        fim_intervalo = inicio + (i + 1) * tamanho_intervalo - 1
        if i == num_processos - 1:
            fim_intervalo = fim
        intervalo.append((inicio_intervalo, fim_intervalo))

    with mp.Pool(processes=num_processos) as pool:
        resultados = pool.starmap(conta_primos_intervalo, intervalo)

    return sum(resultados)


if __name__ == "__main__":
    limite = 1000000

    inicio_tempo = time.time()
    total_primos_seq = conta_primos_sequencial(1, limite)
    tempo_sequencial = time.time() - inicio_tempo

    inicio_tempo = time.time()
    total_primos_par = conta_primos_paralelo(1, limite)
    tempo_paralelo = time.time() - inicio_tempo

    print(f"Total de números primos entre 1 e {limite}: {total_primos_seq}")
    print(f"Tempo de execução sequencial: {tempo_sequencial:.2f} segundos")
    print(f"Tempo de execução paralelo: {tempo_paralelo:.2f} segundos")
    print(f"Ganho de desempenho: {tempo_sequencial / tempo_paralelo:.2f}x")