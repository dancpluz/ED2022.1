#dia que começa / hh:mm:ss (horario de inicio)
#dia que acaba / hh:mm:ss (horario final)

inicio = input().split()
inicio = [inicio[0]] + inicio[1].split(':')
inicio = [int(i) for i in inicio]

fim = input().split()
fim = [fim[0]] + fim[1].split(':')
fim = [int(i) for i in fim]

datas = list(zip(inicio,fim))
#[d,h,m,s]

dhms = [0,0,0,0]

for i in reversed(range(4)):
    dhms[i] = dhms[i] + datas[i][1] - datas[i][0]
    if dhms[i] < 0:
        dhms[i-1] = -1
        if i > 1:
            dhms[i] += 60
        else:
            dhms[i] += 24

for n in dhms:
    if n < 0 or all(n == 0 for n in dhms):
        print('Data inválida!')
        exit()
    

print(f'{dhms[0]} dia(s)\n{dhms[1]} hora(s)\n{dhms[2]} minuto(s)\n{dhms[3]} segundo(s)')


