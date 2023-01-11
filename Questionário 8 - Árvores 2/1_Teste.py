def mostra(arvore, s, a=0):
    print(f'{s*a}{arvore.dado}')
    for i in range(len(arvore.filhos)):
        mostra(arvore.filhos[i], s, a+1)

