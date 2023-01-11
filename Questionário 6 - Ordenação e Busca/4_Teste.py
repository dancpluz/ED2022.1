import math

def bubble(lista):
    for i in reversed(range(len(lista))):
        for j in range(i):
            if lista[j][2] == lista[j+1][2]:
                if lista[j][1] > lista[j+1][1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j] 

lista = []

for _ in range(int(input())):
    tudo = input().split()
    p = int(tudo[0])
    c = int(tudo[1])
    if p == 0:
        media = 0
        lista += [(c, p, 0)]
    else:
        media = math.ceil(c/p)
        lista += [(c, p, media)]

lista.sort(key=lambda x: x[2],reverse=True)
bubble(lista)

for i in lista:
    print(f'{i[2]} / {i[1]}')