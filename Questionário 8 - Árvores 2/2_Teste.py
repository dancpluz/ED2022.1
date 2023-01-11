def mostra_arvore_e_nivel(raiz, n):
    passados = []
    mostra_arvore(raiz, passados)
    if n in passados:
        print(f'\nnivel(raiz, {n}): {nivel(raiz,n)}')
    else:
        print(f'\nnivel(raiz, {n}): -1')

def mostra_arvore(raiz, passados, a=0):
    if raiz != None:
        passados.append(raiz.dado)
        print(f"{a*'_'}{raiz.dado}")
        mostra_arvore(raiz.dir, passados, a+2)
        mostra_arvore(raiz.esq, passados, a+2)

def nivel(raiz, n, c=0):
    if raiz == None:
        return 0
    elif raiz.dado == n:
        return c
    nivel_abaixo = nivel(raiz.esq, n, c+1)
    if nivel_abaixo != 0:
        return nivel_abaixo
    nivel_abaixo = nivel(raiz.dir, n, c+1)
    return nivel_abaixo
    
