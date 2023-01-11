class Tree:
    def __init__(self, chave):
        self.esq = None
        self.dir = None
        self.val = chave

def add(raiz, chave):
    if raiz is None:
        return Tree(chave)
    else:
        if raiz.val == chave:
            return raiz
        elif raiz.val < chave:
            raiz.dir = add(raiz.dir, chave)
        else:
            raiz.esq = add(raiz.esq, chave)
    return raiz

def altura(raiz, d=0, e=0):
    if raiz == None:
        return 0
    direita = altura(raiz.dir, d+1)
    esquerda = altura(raiz.esq, e+1)
    return max(esquerda, direita) + 1


n = input()
numeros = [int(i) for i in input().split()]

raiz = Tree(numeros[0])
del numeros[0]

for i in numeros:
    raiz = add(raiz, i)

print(altura(raiz)-1)
