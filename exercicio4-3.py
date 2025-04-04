class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.is_end = False
        self.prefix = None


class IPv6Trie:
    def __init__(self):
        self.root = TrieNode()

    def ipv6_to_binary(self, ipv6):
        parts = ipv6.split('/')
        ip = parts[0]

        if '::' in ip:
            segments = ip.split('::')
            left = segments[0].split(':') if segments[0] else []
            right = segments[1].split(':') if segments[1] else []
            missing = 8 - len(left) - len(right)
            full = left + ['0'] * missing + right
        else:
            full = ip.split(':')

        binary = ''
        for part in full:
            if part:
                value = int(part, 16)
                binary += format(value, '016b')
            else:
                binary += '0' * 16

        return binary

    def insert(self, prefix):
        parts = prefix.split('/')
        prefix_len = int(parts[1])
        binary = self.ipv6_to_binary(prefix)

        node = self.root
        for i in range(prefix_len):
            bit = int(binary[i])
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

        node.is_end = True
        node.prefix = prefix

    def longest_prefix_match(self, ip):
        binary = self.ipv6_to_binary(ip)
        node = self.root
        matched = None

        for i in range(len(binary)):
            bit = int(binary[i])
            if not node.children[bit]:
                break
            node = node.children[bit]
            if node.is_end:
                matched = node.prefix

        return matched


# Exemplo de uso
trie = IPv6Trie()
trie.insert("2001:db8::/32")
trie.insert("2001:db8:1234::/48")
result = trie.longest_prefix_match("2001:db8:1234:5678::1")
print("resultado:  "+result)  # Deve retornar "2001:db8:1234::/48"