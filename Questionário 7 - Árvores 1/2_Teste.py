def mostra(r):
    if r == None:
        print('()', end='')
        return
    print(f'({r.dado} ', end='')
    mostra(r.esq)
    print(' ', end='')
    mostra(r.dir)
    print(')', end='')

