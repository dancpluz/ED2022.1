def decompress(x,result='',string=''):
    if x < 1:
        if result == '':
            return string
        elif len(result) >= 5:
            binario = result[:5]
            decimal = int(binario[::-1], 2)
            string += chr(decimal+64)
            return decompress(x,result[5:],string)
        else:
            decimal = int(result[::-1], 2)
            string += chr(decimal+64)
            result = ''
            return decompress(x,result,string)
    else:
        result += str(x % 2)
        return decompress(x//2, result)

