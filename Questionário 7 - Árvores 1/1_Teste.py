def mostra_arvore_e_altura(raiz):
    mostra_arvore(raiz)
    if raiz == None:
        print(f'\naltura: {altura(raiz)}')
    else:
        print(f'\naltura: {altura(raiz)-1}')


def mostra_arvore(raiz, a=0):
    if raiz != None:
        print(f"{a*'_'}{raiz.dado}")
        mostra_arvore(raiz.dir, a+2)
        mostra_arvore(raiz.esq, a+2)


def altura(raiz, d=0, e=0):
    if raiz == None:
        return 0
    direita = altura(raiz.dir, d+1)
    esquerda = altura(raiz.esq, e+1)
    return max(esquerda, direita) + 1
