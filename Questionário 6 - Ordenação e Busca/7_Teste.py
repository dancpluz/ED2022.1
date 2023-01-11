def bubble(lista):
    for i in reversed(range(len(lista))):
        for j in range(i):
            atual = lista[j]
            proximo = lista[j+1]
            if atual[0] < proximo[0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            elif atual[0] == proximo[0]:
                if atual[1] % 2 != 0 and proximo[1] % 2 == 0:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                elif atual[1] % 2 == 0 and proximo[1] % 2 == 0:
                    if atual[1] < proximo[1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
                elif atual[1] % 2 != 0 and proximo[1] % 2 != 0:
                    if atual[1] > proximo[1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]

entrada = input().split()
n = int(entrada[0])
k = int(entrada[1])
numeros = []

for _ in range(n):
    num = int(input())
    mod = abs(num) % k
    if num < 0:
        numeros += [(-mod,num)]
    else:
        numeros += [(mod,num)]

bubble(numeros)

for n in numeros:
    print(n[1],end=' ')
