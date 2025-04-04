class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return self

        current = self.root

        while True:
            if value == current.value:
                return None
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return self
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return self
                current = current.right

    def search(self, value):
        if self.root is None:
            return False

        current = self.root
        found = False

        while current and not found:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True

        return current if found else False


bst = BinarySearchTree()

print("Insira os valores para a árvore (digite 'fim' para parar):")
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    try:
        valor = int(entrada)
        bst.insert(valor)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


def imprimir_arvore(node, prefixo="", eh_ultimo=True):
    if node is not None:
        print(prefixo + ("└── " if eh_ultimo else "├── ") + str(node.value))

        # Prepara o prefixo para os filhos
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")

        # Imprime filho da direita depois o da esquerda (para melhor visualização)
        if node.right is not None or node.left is not None:
            imprimir_arvore(node.right, novo_prefixo, node.left is None)
            imprimir_arvore(node.left, novo_prefixo, True)


print("\nÁrvore construída:")
imprimir_arvore(bst.root)

valor_busca = int(input("\nDigite o valor a ser buscado: "))
resultado = bst.search(valor_busca)

if resultado:
    print(f"Elemento {valor_busca} encontrado!")
else:
    print(f"Elemento {valor_busca} não encontrado.")