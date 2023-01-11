# enqueue X -> solicitação com X > 0 processos a fila. entrada para 2 comandos:
# P = prioridade sendo o menor de maior prioridade.
# P scramble C -> acobertar o processo, C = string, alterado de acordo com '(' e ')'
# P dekey O S -> remover ruídos, O = inteiro(num de operações na sequência S) , S = lista int
# cada operação envolve (i) retirar 2 elementos do início da sequência (A e B) e,
# se A<B então adiciona A ao final da sequência S e B ao início; caso contrário adiciona A
# ao início da sequência S e B ao final. É garantido que há pelo menos 2 inteiros em S.
# Ao final, a função apresenta a junção de todos os números, determinando o novo endereço
# de memória a ser usado. É garantido que todo inteiro da sequência é positivo.
# stop -> interrompe a execução e mostra quantos comandos não foram executados.
# go -> executa o próximo comando temp disponível na fila de processamento.

class Fila:
    def __init__(self):
        self.items = []

    def tamanho(self):
        return len(self.items)

    def entrar(self, item):
        index = 0
        for i in range(len(self.items)):
            if item[0] > self.items[i][0]:
                index += 1
            elif item[0] == self.items[i][0]:
                index += 1
                break
        self.items.insert(index, item)

    def sair(self):
        return self.items.pop(0)

    def executar(self):
        try:
            if self.items[0][1] == 'dekey':
                self.dekey(self.items[0][2], self.items[0][3])
            else:
                self.scramble(self.items[0][2])
        except:
            pass

    def scramble(self, string):
        inicio = 0
        lista = []
        aberto = False

        for i in string:
            if i == '(':
                if aberto:
                    inicio = 0
                aberto = True
            elif i == ')':
                inicio = 0
                aberto = False
            else:
                if aberto:
                    lista.insert(inicio, i)
                    inicio += 1
                else:
                    lista.append(i)

        if lista:
            print(''.join(lista))
        self.sair()

    def dekey(self, num, seq):
        for _ in range(num):
            if seq[0] < seq[1]:
                seq.append(seq[0])
                seq.pop(0)
            else:
                seq.append(seq[1])
                seq.pop(1)
        print(*seq, sep='')
        self.sair()


fila = Fila()
fim = False

while not fim:
    entrada = input().split()
    comando = entrada[0]

    if comando == 'stop':
        print(f'{fila.tamanho()} processo(s) órfão(s).')
        fim = True
    elif comando == 'enqueue':
        x = int(entrada[1])
        for _ in range(x):
            temp = input().split()
            prioridade = int(temp[0])
            com = temp[1]

            if com == 'scramble':
                sequencia = temp[2]
                fila.entrar((prioridade, com, sequencia))
            else:
                op = int(temp[2])
                sequencia_int = [int(i) for i in temp[3:]]
                fila.entrar((prioridade, com, op, sequencia_int))
    elif comando == 'go':
       fila.executar()