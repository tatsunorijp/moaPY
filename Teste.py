import math
import heapq
def main():

    matrizAux = input()
    matriz = list(map(int, matrizAux.split()))

    no = No(matriz, 0, findZero(matriz))
    listaAberta = []
    heapq.heappush(listaAberta, no)
    listaFechada = set()

    while(listaAberta):
        noProcessando = heapq.heappop(listaAberta)

        if(noProcessando.h == 0):
            print(noProcessando.g)
            break

        if(noProcessando in listaFechada):
            continue

            
        listaFechada.add(noProcessando)


        if(noProcessando.i not in [0, 1, 2, 3]):
            noAux = No(changeTop(noProcessando.matriz, noProcessando.i), noProcessando.g + 1, (noProcessando.i)-4)
            if(noAux not in listaFechada):
                heapq.heappush(listaAberta, noAux)

        if(noProcessando.i not in [12, 13, 14, 15]):
            noAux = No(changeDown(noProcessando.matriz, noProcessando.i), noProcessando.g + 1, (noProcessando.i)+4)
            if (noAux not in listaFechada):
                heapq.heappush(listaAberta, noAux)

        if(noProcessando.i not in [0, 4, 8, 12]):
            noAux = No(changeLeft(noProcessando.matriz, noProcessando.i), noProcessando.g + 1, (noProcessando.i)-1)
            if (noAux not in listaFechada):
                heapq.heappush(listaAberta, noAux)

        if(noProcessando.i not in [3, 7, 11, 15]):
            noAux = No(changeRight(noProcessando.matriz, noProcessando.i), noProcessando.g + 1, (noProcessando.i)+1)
            if (noAux not in listaFechada):
                heapq.heappush(listaAberta, noAux)

class No:
    def __init__(self, matriz, g, i):
        self.matriz = matriz
        self.g = g
        self.h = heuristica3(matriz)
        self.f = g + self.h
        self.i = i

    def __lt__(self, o):
        return self.f < o.f

def changeTop(matriz, i):
    novaMatriz = matriz[:]
    x = i//4
    x = x - 1
    y = i % 4
    j = (x*4) + y

    novaMatriz[i] = novaMatriz[j]
    novaMatriz[j] = 0

    return novaMatriz
def changeDown(matriz, i):
    novaMatriz = matriz[:]
    x = i // 4
    x = x + 1
    y = i % 4
    j = (x * 4) + y

    novaMatriz[i] = novaMatriz[j]
    novaMatriz[j] = 0
    return novaMatriz
def changeLeft(matriz, i):
    novaMatriz = matriz[:]
    x = i // 4
    y = i % 4
    y = y - 1
    j = (x * 4) + y

    novaMatriz[i] = novaMatriz[j]
    novaMatriz[j] = 0
    return novaMatriz
def changeRight(matriz, i):
    novaMatriz = matriz[:]
    x = i // 4
    y = i % 4
    y = y + 1
    j = (x * 4) + y

    novaMatriz[i] = novaMatriz[j]
    novaMatriz[j] = 0

    return novaMatriz

def findZero(matriz):
    for i in range(16):
        if (matriz[i]) == 0:
            return i
    return 0

def heuristica3(matriz):
    resp = 0
    for i in range(16):
        resp = resp + heuristica3pt2dois(i, matriz[i])
    return resp

def heuristica3pt2(posicao, elemento):
    formaCorreta = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]
    for i2 in range(16):
        if((formaCorreta[i2] == elemento) and (elemento!=0)):
            x = i2//4
            y = i2 % 4
            x2 = posicao // 4
            y2 = posicao % 4
            return int((math.fabs(x2 - x) + math.fabs(y2 - y)))

    return 0

def heuristica3pt2dois(posicao, elemento):
    vetor = [0, 0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4, 5, 6, 10]

    if(elemento) == 0:
        return 0

    x = vetor[elemento] // 4
    y = vetor[elemento] % 4
    x2 = posicao // 4
    y2 = posicao % 4

    return int((math.fabs(x2 - x) + math.fabs(y2 - y)))
main()