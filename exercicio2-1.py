import multiprocessing as mp
from functools import partial
import time
import matplotlib.pyplot as plt


def somar_parte(inicio, fim):
    return sum(range(inicio, fim + 1))


def soma_paralela(inicio, fim, num_processos=None):
    if num_processos is None:
        num_processos = mp.cpu_count()

    pool = mp.Pool(processes=num_processos)
    tamanho_total = fim - inicio + 1
    tamanho_parte = tamanho_total // num_processos

    partes = [(inicio + i * tamanho_parte,
               inicio + (i + 1) * tamanho_parte - 1 if i < num_processos - 1 else fim)
              for i in range(num_processos)]

    resultados = pool.starmap(somar_parte, partes)
    pool.close()
    pool.join()

    return sum(resultados)


def soma_sequencial(inicio, fim):
    return sum(range(inicio, fim + 1))


def comparar_desempenho(inicio, fim):
    tempos = {"Sequencial": [], "Paralelo": []}
    resultados = {}

    print(f"Comparando somas de {inicio} até {fim}")

    inicio_tempo = time.time()
    resultado_seq = soma_sequencial(inicio, fim)
    fim_tempo = time.time()
    tempo_seq = fim_tempo - inicio_tempo
    tempos["Sequencial"].append(tempo_seq)
    resultados["Sequencial"] = resultado_seq
    print(f"Soma sequencial: {resultado_seq}, Tempo: {tempo_seq:.4f} segundos")

    inicio_tempo = time.time()
    resultado_par = soma_paralela(inicio, fim)
    fim_tempo = time.time()
    tempo_par = fim_tempo - inicio_tempo
    tempos["Paralelo"].append(tempo_par)
    resultados["Paralelo"] = resultado_par
    print(f"Soma paralela: {resultado_par}, Tempo: {tempo_par:.4f} segundos")

    speedup = tempo_seq / tempo_par
    print(f"Speedup: {speedup:.2f}x")

    return tempos, resultados


def plotar_comparacao(tempos):
    metodos = list(tempos.keys())
    valores = [tempos[metodo][0] for metodo in metodos]

    plt.figure(figsize=(10, 6))
    barras = plt.bar(metodos, valores, color=['blue', 'green'])

    plt.title('Comparação de Tempo: Soma Sequencial vs Paralela')
    plt.xlabel('Método')
    plt.ylabel('Tempo (segundos)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2., altura + 0.05,
                 f'{altura:.4f}s', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('comparacao_soma.png')
    plt.close()

    print("Gráfico salvo como 'comparacao_soma.png'")


if __name__ == "__main__":
    inicio = 1
    fim = 10000000

    tempos, resultados = comparar_desempenho(inicio, fim)
    plotar_comparacao(tempos)