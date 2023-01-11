class Stack:
    def __init__(self,list):
        self.items = list
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

def check(s):
    for i in range(len(s)-1):
        if s[i] == '(' and s[i+1] in '[{':
            s.insert(i+1, 'x')
        elif s[i] == '[' and s[i+1] in '({':
            s.insert(i+1, 'x')
        elif s[i] == '{' and s[i+1] in '([':
            s.insert(i+1, 'x')

n_input = int(input())

while n_input > 0:
    string = list(input())
    check(string)
    s = Stack(string)
    duplicata = False

    for i in s.items:
        if i in ')]}':
            topo = s.pop()
            outros_caracteres = 0

            while topo not in '([{':
                outros_caracteres += 1
                topo = s.pop()

            if outros_caracteres < 1:
                duplicata = True
                break
        else:
            s.push(i)
    
    if duplicata:
        print('A expressão possui duplicata.')
        n_input -= 1
    else:
        print('A expressão não possui duplicata.')
        n_input -= 1
    
