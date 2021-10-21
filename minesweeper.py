import random
class Minesweeper:
    def __init__(self, n, m, k):
        self.n = 0
        self.m = 0
        self.k = 0

    def difficulty(x):
        diff = input("choose a difficulty: ")
        if diff == 

    def generateMines(n, m, k):

        for i in k:
            random.randint(n)

    def generateBoard(n, m, k):
        array = [[0 for i in range(n)] for i in range(m)]

        for i in range(0,k):
            x, y = random.randint(0,n-1), random.randint(0,m-1)
            array[x][y] = "M"
        print(array)

    def printBoard():
        pass
