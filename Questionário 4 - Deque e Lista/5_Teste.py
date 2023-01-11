#inserir na lista num/pos/back
#back será calculado como index na lista - numero dado
#se numero dado == 0 -> None
#se index > numero dado -> None
#quando remover, diminuir todos elementos após back -1
#botar None se o back = index do removido

def remover_back(i):
    global lista
    subtrair = False

    for e in lista[i:]:
        if subtrair:
            if e[2] == 0:
                if i != 0:
                    pass
                else:
                    e[2] = None
            elif e[2] != None:
                e[2] -= 1

        elif e[2] == i:
            e[2] = None
            subtrair = True

lista = []
tempo = -1

entrada = input().split()
while entrada[0] != 'f':
    comando = entrada[0]
    valor = [int(x) for x in entrada[1:]]
    tempo += 1
    index = len(lista)

    if comando == 'i':
        back = index - valor[1]
        if valor[1] == 0 or index < valor[1]:
            back = None
        lista.append([valor[0],tempo,back])
    else:
        for l in lista:
            if valor[0] == l[0]:
                remover_back(lista.index(l))
                lista.remove(l)
    entrada = input().split()
    
if lista == []:
    print(-1)

for p in lista:
    if p[2] == None:
        print(f'[{p[0]},{p[1]}]',end=' ')
    else:
        print(f'[{p[0]},{p[1]},{p[2]}]',end=' ')