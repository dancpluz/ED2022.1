def rotaciona_esquerda(raiz):
    if raiz is None:
        return raiz
    raiz_rodada = raiz.dir
    try:
        temp = raiz_rodada.esq
    except:
        return raiz
    raiz_rodada.esq = raiz
    raiz.dir = temp
    return raiz_rodada
