def constituiArvoreBinariaDeBusca(raiz):
    global antes
    antes = None
    return ArvoreBinariaCheck(raiz)

def ArvoreBinariaCheck(raiz):
    global antes
    if raiz is None:
        return True
    elif ArvoreBinariaCheck(raiz.esq) == False:
        return False
    if antes != None and antes.dado > raiz.dado:
        return False
    antes = raiz
    return ArvoreBinariaCheck(raiz.dir)
