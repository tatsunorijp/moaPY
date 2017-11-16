import math


def main():
    matriz = []
    for i in range(4):
        matriz.append([0]*4)
    print('Digite as posições iniciais\n')
    for i in range(4):
        for j in range(4):
            matriz[i][j] = int(input())

    no = No(matriz, None, 0)

    print('Matriz: \n')
    print(no.matriz[0])
    print(no.matriz[1])
    print(no.matriz[2])
    print(no.matriz[3], "\n")

    print('G: %d, H: %d, F: %d'%(no.g, no.h, no.f))



class No:
    def __init__(self, matriz, pai, g):
        self.matriz = matriz
        self.pai = pai
        self.g = g
        self.h = heuristica3(self.matriz)
        self.f = g + self.h

def heuristica1(matriz):
    formaCorreta = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]]
    valor = 0

    for i in range(4):
        for j in range(4):
            if(matriz[i][j] != formaCorreta[i][j] and matriz[i][j] != 0):
                   valor = valor +1
    return valor

def heuristica3(matriz):
    resp = 0
    for i in range(4):
        for j in range(4):
            resp = resp + heuristica3pt2(i, j, matriz[i][j])

    return resp

def heuristica3pt2(i, j, elemento):
    formaCorreta = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]]

    for i2 in range(4):
        for j2 in range(4):
            if((formaCorreta[i2][j2] == elemento) and (elemento!=0)):
                return int((math.fabs(i2 - i) + math.fabs(j2 -j)))
    return 0

main()