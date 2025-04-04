import time
import random
import matplotlib.pyplot as plt


def ip_to_binary(ip):
    parts = ip.split('.')
    binary = ""
    for part in parts:
        binary += bin(int(part))[2:].zfill(8)
    return binary


def linear_search(ip, prefixes):
    ip_binary = ip_to_binary(ip)
    longest_match = None
    longest_length = -1

    for prefix, length in prefixes:
        prefix_binary = ip_to_binary(prefix)
        if ip_binary[:length] == prefix_binary[:length] and length > longest_length:
            longest_match = prefix
            longest_length = length

    return longest_match


class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.prefix = None


def insert_into_trie(root, prefix, length, original_prefix):
    node = root
    for i in range(length):
        bit = int(prefix[i])
        if node.children[bit] is None:
            node.children[bit] = TrieNode()
        node = node.children[bit]
    node.prefix = original_prefix


def build_trie(prefixes):
    root = TrieNode()
    for prefix, length in prefixes:
        prefix_binary = ip_to_binary(prefix)
        insert_into_trie(root, prefix_binary, length, prefix)
    return root


def trie_search(ip, trie_root):
    ip_binary = ip_to_binary(ip)
    node = trie_root
    longest_match = None

    for i in range(32):
        if i >= len(ip_binary):
            break
        bit = int(ip_binary[i])
        if node.children[bit] is None:
            break
        node = node.children[bit]
        if node.prefix is not None:
            longest_match = node.prefix

    return longest_match


def generate_prefixes(count):
    prefixes = []
    for _ in range(count):
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        length = random.randint(1, 32)
        prefixes.append((ip, length))
    return prefixes


def compare_performance():
    sizes = [100, 500, 1000, 2000, 5000]
    linear_times = []
    trie_times = []
    test_ip = "192.168.1.55"

    for size in sizes:
        prefixes = generate_prefixes(size)

        start_time = time.time()
        linear_result = linear_search(test_ip, prefixes)
        linear_time = time.time() - start_time
        linear_times.append(linear_time)

        trie_root = build_trie(prefixes)
        start_time = time.time()
        trie_result = trie_search(test_ip, trie_root)
        trie_time = time.time() - start_time
        trie_times.append(trie_time)

        print(f"Tamanho: {size} prefixos")
        print(f"  Tempo da busca linear: {linear_time:.6f} segundos")
        print(f"  Tempo da busca Trie: {trie_time:.6f} segundos")
        print(f"  A busca Trie é {linear_time / trie_time:.2f}x mais rápida")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, marker='o', label='Busca Linear')
    plt.plot(sizes, trie_times, marker='s', label='Busca Trie')
    plt.xlabel('Número de Prefixos')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Desempenho: Busca Linear vs. Trie para Prefixos IPv4')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparacao_desempenho.png')
    plt.show()


if __name__ == "__main__":
    compare_performance()