n = int(input())

for _ in range(n):
    plano = [i for i in input()]
    fim = False

    for _ in range(3):
        for i in input():
            if i in plano:
                plano.remove(i)
            else:
                fim = True
                break
    if fim == True:
        print('You died!')
    elif plano != []:
        plano = [i for n, i in enumerate(plano) if i not in plano[:n]]
        plano.sort()
        print('Bora ralar: ',end='')
        print(*plano,sep='')
    else:
        print("It's in the box!")
