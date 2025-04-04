import time
import random
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)


def measure_performance():
    sizes = [500, 1000, 2000, 3000, 4000, 5000]
    in_order_times = []
    pre_order_times = []
    post_order_times = []

    for size in sizes:
        bst = BinarySearchTree()
        values = random.sample(range(1, size * 10), size)

        for value in values:
            bst.insert(value)

        start_time = time.time()
        bst.in_order()
        in_order_times.append((time.time() - start_time) * 1000)

        start_time = time.time()
        bst.pre_order()
        pre_order_times.append((time.time() - start_time) * 1000)

        start_time = time.time()
        bst.post_order()
        post_order_times.append((time.time() - start_time) * 1000)

    return sizes, in_order_times, pre_order_times, post_order_times


def plot_performance(sizes, in_order_times, pre_order_times, post_order_times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, in_order_times, 'o-', label='In-Ordem', color='blue')
    plt.plot(sizes, pre_order_times, 's-', label='Pré-Ordem', color='green')
    plt.plot(sizes, post_order_times, '^-', label='Pós-Ordem', color='red')

    plt.title('Comparação de Performance dos Percursos em Árvore Binária de Busca')
    plt.xlabel('Tamanho da Árvore (número de nós)')
    plt.ylabel('Tempo de Execução (ms)')
    plt.legend()
    plt.grid(True)

    plt.savefig('bst_traversal_performance.png')
    plt.show()


def main():
    print("Medindo a performance dos algoritmos de percurso...")
    sizes, in_order_times, pre_order_times, post_order_times = measure_performance()

    print("\nTamanhos das árvores:", sizes)
    print("Tempos In-Ordem (ms):", [round(t, 2) for t in in_order_times])
    print("Tempos Pré-Ordem (ms):", [round(t, 2) for t in pre_order_times])
    print("Tempos Pós-Ordem (ms):", [round(t, 2) for t in post_order_times])

    plot_performance(sizes, in_order_times, pre_order_times, post_order_times)

    print("\nAnálise comparativa:")
    print("Todos os três algoritmos têm complexidade O(n), onde n é o número de nós na árvore,")
    print("pois cada algoritmo visita exatamente uma vez cada nó da árvore.")
    print("Qualquer diferença de performance entre os algoritmos geralmente é atribuída a")
    print("fatores como gerenciamento de memória e otimizações do interpretador Python,")
    print("não a diferenças fundamentais na complexidade dos algoritmos.")


if __name__ == "__main__":
    main()