def duplicata(roupa):
    global passados
    
    for i in passados:
        if roupa == i:
            return True
    return False

n = input()
roupas = input().split()
passados = []
cont = 0

for r in roupas:
    if duplicata(r):
        cont += 1
        passados += [r]
    else:
        passados += [r]

print(cont)