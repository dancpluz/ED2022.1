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

def infixa(raiz):
    if raiz != None:
        infixa(raiz.esq)
        print(f"{raiz.val}", end=' ')
        infixa(raiz.dir)

def prefixa(raiz):
    if raiz != None:
        print(f"{raiz.val}", end=' ')
        prefixa(raiz.esq)
        prefixa(raiz.dir)

def posfixa(raiz):
    if raiz != None:
        posfixa(raiz.esq)
        posfixa(raiz.dir)
        print(f"{raiz.val}", end=' ')

primeiro = True
raiz = None
fim = False

while not fim:
    entrada = input()
    if entrada == 'quack':
        fim = True
    elif entrada == 'in':
        infixa(raiz)
        print()
    elif entrada == 'pre':
        prefixa(raiz)
        print()
    elif entrada == 'pos':
        posfixa(raiz)
        print()
    elif primeiro:
        raiz = Tree(int(entrada))
        primeiro = False
    else:
        raiz = add(raiz,int(entrada))
