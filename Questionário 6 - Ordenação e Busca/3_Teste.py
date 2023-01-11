paulo = [int(i) for i in input().split()]
soma = 2 * paulo[0] + 3 * paulo[1] + paulo[2]
paulo += [soma]
pos = 1

lista = []
for _ in range(int(input())):
    l = [int(i) for i in input().split()]
    soma = 2 * l[0] + 3 * l[1] + l[2]
    l += [soma]
    lista += [l]

for i in lista:
    if i[4] > paulo[4]:
        pos += 1
    elif i[4] == paulo[4]:
        if i[3] >= 60 and paulo[3] < 60:
            pos += 1
        elif i[3] < 60 and paulo[3] >= 60:
            pass
        else:
            if i[1] > paulo[1]:
                pos += 1
            elif i[1] == paulo[1]:
                if i[0] > paulo[0]:
                    pos += 1
                elif i[0] == paulo[0]:
                    if i[3] > paulo[3]:
                        pos += 1

print(pos)