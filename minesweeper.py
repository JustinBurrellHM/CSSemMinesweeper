import random
class Minesweeper:
    # def __init__(self, n, m, k):
    #     self.n = 0
    #     self.m = 0
    #     self.k = 0

    def generate_board(n,m,k):
        array = [[0 for i in range(n)] for i in range(m)]
        for i in range(0,k):
            x, y = random.randint(0,n-1), random.randint(0,m-1)
            array[x][y] = "M"
        return array
    
    def difficulty():
        diff = input("choose a difficulty: ")
        if diff == "Easy":
            print(generate_board(6,6,6))
        elif diff == "Medium":
            print(generate_board(12,12,10))
        elif diff == "Hard":
            print(generate_board(16,16,16))

    def print_board(l):
        for row in l:
            for col in row:
                print(col, end=' ')
            print()
    # found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853
