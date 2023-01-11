def maior_norma(v1,v2):
    v1 = [abs(i) for i in v1]
    v2 = [abs(i) for i in v2]

    if sum(v1) > sum(v2):
        print('PRIMEIRO')
    else:
        print('SEGUNDO')