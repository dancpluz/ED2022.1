def verificaPontuacao(raiz,v1,v2):
    pontuacao(raiz,v1,v2)

def pontuacao(raiz,v1,v2,cartas=[],procura=False):
    if raiz is None:
        return 
    if procura and not v2:
        None
    elif procura and not v1:
        None
    elif raiz.dado == v1:
        return pontuacao(raiz, v1, False, cartas, True)
    if raiz.dado == v2:
        return pontuacao(raiz, False, v2, cartas, True)
    

    pontuacao(raiz,v1,v2)
