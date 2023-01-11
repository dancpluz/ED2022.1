def getElementById(raiz, s):
    lista = []
    return main(raiz,s,lista)

def main(raiz, s, lista):
    if type(raiz) == str:
        return
    for i in raiz:
        if i == s:
            lista += [i]
        elif '*' in s:
            if s.strip('*').lower() in i.lower():
                lista += [i]
        main(raiz[i], s, lista)
    return lista


raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},
                 'BODY': {'H1': 'Cabeçalho', 'p': 'Parágrafo'}}}


print(sorted(getElementById(raiz, 'H1')))
print(sorted(getElementById(raiz, 'H*')))
