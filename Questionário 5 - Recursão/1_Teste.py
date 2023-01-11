def peronio(a, b, n=0):
    try:
        if a[0] == b[0]:
            return peronio(a[1:], b[1:], n+1)
        else:
            return n+1
    except:
        return n+1
