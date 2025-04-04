class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix = None


class IPv4Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix):
        ip, mask = prefix.split('/')
        mask = int(mask)
        octets = list(map(int, ip.split('.')))

        node = self.root
        bits_processed = 0

        for i in range(4):
            octet = octets[i]
            for bit_pos in range(7, -1, -1):
                bit = (octet >> bit_pos) & 1

                bits_processed += 1
                if bits_processed > mask:
                    node.prefix = prefix
                    return

                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

                if bits_processed == mask:
                    node.prefix = prefix
                    return

    def longest_prefix_match(self, ip):
        octets = list(map(int, ip.split('.')))

        node = self.root
        best_match = None

        for i in range(4):
            octet = octets[i]
            for bit_pos in range(7, -1, -1):
                bit = (octet >> bit_pos) & 1

                if node.prefix:
                    best_match = node.prefix

                if bit not in node.children:
                    return best_match

                node = node.children[bit]

        return node.prefix if node.prefix else best_match


def test_ipv4_trie():
    trie = IPv4Trie()
    prefixes = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]

    for prefix in prefixes:
        trie.insert(prefix)

    result = trie.longest_prefix_match("192.168.1.100")
    print(f"Longest prefix match for 192.168.1.100: {result}")


test_ipv4_trie()