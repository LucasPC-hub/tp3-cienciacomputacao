class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def eh_bst_valida(raiz):
    return verificar_bst(raiz, float('-inf'), float('inf'))


def verificar_bst(no, minimo, maximo):
    if no is None:
        return True

    if no.valor <= minimo or no.valor >= maximo:
        print(f"Violação: Nó {no.valor} fora dos limites [{minimo}, {maximo}]")
        return False

    print(f"Verificando nó {no.valor} com limites [{minimo}, {maximo}]")

    esquerda_valida = verificar_bst(no.esquerda, minimo, no.valor)
    direita_valida = verificar_bst(no.direita, no.valor, maximo)

    return esquerda_valida and direita_valida


raiz = Node(10)
raiz.esquerda = Node(5)
raiz.direita = Node(15)
raiz.esquerda.esquerda = Node(3)
raiz.esquerda.direita = Node(7)
raiz.direita.esquerda = Node(12)
raiz.direita.direita = Node(18)

print("Verificando árvore original:")
resultado = eh_bst_valida(raiz)
print("A árvore é uma BST válida:", resultado)

print("\nAlterando nó 7 para 11...")
raiz.esquerda.direita.valor = 11
print("Verificando árvore modificada:")
resultado = eh_bst_valida(raiz)
print("Após alteração, a árvore é uma BST válida:", resultado)