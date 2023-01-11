class Tree:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def filho(self, dado):
        self.filhos.append(dado)

    def gametree(self,nivel=0):
        print(f'{nivel*"__"}?')
        for f in self.filhos:
            if f.filhos == []:
                print(f'{(nivel+1)*"__"}{f.dado}')
            else:
                f.gametree(nivel+1)

    def probtree(self,n=0,soma=0,nivel=0):
        if self.dado == '?':
            for f in self.filhos:
                if type(f) == str:
                    n += 1
                    if f == 'V':
                        soma += 1.0
                else:
                    f.probtree(n,soma,nivel+1)
                    if n == 0:
                        print(f'{nivel*".."}? {soma}')
                    else:
                        print(f'{nivel*".."}? {soma/n}')
class Queue:
    def __init__(self):
        self.elementos = [] 
    
    def first(self):
        return self.elementos[0]

    def add(self,value):
        self.elementos.append(value)

    def pop(self):
        self.elementos.pop(0)

    def isEmpty(self):
        return self.elementos == []

def entrada(inp):
    split = inp.split()
    if len(split) == 1:
        return split[0], None
    return split[0], int(split[1])

def criar_arvore(f,d,n):
    lista_a.pop()
    lista_p.pop()
    for _ in range(n):
        d,n = entrada(input())
        if d == '?':
            lista_a.add(Tree(d))
            lista_p.add(n)
            f.filho(Tree(d))
        else:
            f.filho(Tree(d))

lista_a = Queue()
lista_p = Queue()
d,n = entrada(input())
raiz = Tree(d)
for _ in range(n):
    d,n = entrada(input())
    if d == '?':
        lista_a.add(Tree(d))
        lista_p.add(n)
        raiz.filho(Tree(d))
    else:
        raiz.filho(Tree(d))

while not lista_a.isEmpty():
    d = lista_a.first()
    n = lista_p.first()
    lista_p.pop()
    lista_a.pop()

    for f in raiz.filhos:
        criar_arvore(f,d,n)

raiz.gametree()


