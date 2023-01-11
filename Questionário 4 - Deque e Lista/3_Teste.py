lista = []
entrada = input()

while entrada != 'fim':
    nome_preço = entrada.split()
    nome = nome_preço[0]
    preço = nome_preço[1]

    if nome == '-':
        for index in range(len(lista)):
            if lista[index][0] == preço:
                lista.pop(index)
                break
    else:
        lista += [[nome, float(preço)]]
    entrada = input()

lista.sort(reverse=True,key=lambda x: x[1])

soma = 0
for i in lista:
    print(f'{i[0]}: R$ {i[1]:.2f}')
    soma += i[1]

print('-'*22)
print(f'{len(lista)} item(ns): R$ {soma:.2f}')