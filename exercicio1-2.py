class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = Node(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = Node(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def percurso_inorder(self):
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, no, resultado):
        if no:
            self._inorder_recursivo(no.esquerda, resultado)
            resultado.append(no.valor)
            self._inorder_recursivo(no.direita, resultado)

    def encontrar_minimo(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def deletar(self, valor):
        self.raiz = self._deletar_recursivo(self.raiz, valor)

    def _deletar_recursivo(self, no, valor):
        if no is None:
            return None

        if valor < no.valor:
            no.esquerda = self._deletar_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._deletar_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            sucessor = self.encontrar_minimo(no.direita)
            no.valor = sucessor.valor
            no.direita = self._deletar_recursivo(no.direita, sucessor.valor)

        return no


arvore = ArvoreBinariaBusca()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(valor)

print("Percurso in-order inicial:", arvore.percurso_inorder())

arvore.deletar(20)
print("Após remover 20:", arvore.percurso_inorder())

arvore.deletar(30)
print("Após remover 30:", arvore.percurso_inorder())

arvore.deletar(50)
print("Após remover 50:", arvore.percurso_inorder())