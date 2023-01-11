def quadrado(l):
    if len(l) < 2:
        print(l[0])
        return
    print(f'{l[0]} + soma({l[1:]})')
    return quadrado(l[1:])

lista = []
cont = int(input())
c = cont
result = cont ** 2
n = 1

while cont > 0:
    if n % 2 != 0:
        lista += [n]
        n += 2
        cont -= 1

quadrado(lista)
print(15*'-')
print(f'{c} ** 2 == {result}')
