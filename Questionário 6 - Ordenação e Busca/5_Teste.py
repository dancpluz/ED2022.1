def ordem_str(a,b):
    if [a,b] == sorted([a,b]):
        return False
    return True

def bubble(lista):
    for i in reversed(range(len(lista))):
        for j in range(i):
            atual = lista[j]
            proximo = lista[j+1]
            if atual[1] < proximo[1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            elif atual[1] == proximo[1]:
                if atual[2] < proximo[2]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                elif atual[2] == proximo[2]:
                    if atual[3] < proximo[3]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
                    elif atual[3] == proximo[3]:
                        if atual[4] < proximo[4]:
                            lista[j], lista[j+1] = lista[j+1], lista[j]
                        elif atual[4] == proximo[4]:
                            if atual[5] < proximo[5]:
                                lista[j], lista[j+1] = lista[j+1], lista[j]
                            elif atual[5] == proximo[5]:
                                if ordem_str(atual[0],proximo[0]):
                                    lista[j], lista[j+1] = lista[j+1], lista[j]

lista = []

for _ in range(20):
    t = input().split()

    pontos = 0
    vitorias = 0
    gols = 0
    gols_contra = 0
    time = t[0]

    for i in t[1:]:
        p = int(i[0])
        c = int(i[2])

        if p > c:
            pontos += 3
            vitorias += 1
            gols += p
            gols_contra += c
        elif p < c:
            gols += p
            gols_contra += c
        else:
            pontos += 1
            gols += p
            gols_contra += c
    lista += [(time,pontos,vitorias,gols-gols_contra,gols,gols_contra)]

bubble(lista)

soma_total = 0
liberadores = [i[0] for i in lista[:4]]
rebaixados = [i[0] for i in reversed(lista[-4:])]

for i in lista:
    soma_total += i[1]

print(f'Media de pontos: {soma_total/20:.2f}')
print('Liberadores: ',end='')
print(*liberadores,sep=', ')
print('Rebaixados: ', end='')
print(*rebaixados,sep=', ')