import random

class Array:
    def __init__(self):
        self.n = 0 # num columns
        self.m = 0 # num rows 
        self.k = 0 # num of mines
        self.array = []
        self.set_difficulty()    
    def set_difficulty(self):
        difficulty = input("What difficult do you want: Easy, Medium, or Hard? ")
        if difficulty == "Easy":
            self.n = 5
            self.m = 6
            self.k = 3
            self.array = [[0 for i in range(self.n)] for i in range(self.m)]
        elif difficulty == "Medium":
            self.n = 8
            self.m = 8
            self.k = 6
            self.array = [[0 for i in range(self.n)] for i in range(self.m)]
        elif difficulty == "Hard":
            self.n = 12
            self.m = 12
            self.k = 12
            self.array = [[0 for i in range(self.n)] for i in range(self.m)]
        
    def generate_board(self):
        print(self.n, self.m, self.k)
        for i in range(0, self.k):
            y, x = random.randint(0, self.n-1), random.randint(0, self.m-1)
            print('n, m', self.n, self.m)
            print('x, y', x, y)
            while self.array[y][x] == "M":
                y, x = random.randint(0, self.n-1), random.randint(0, self.m-1)
            self.array[y][x] = "M"
            print('m')

        return self.array

    def check_mines(self, x, y):
        #counter variable 
        counter = 0
        print(x, y)
        # iterate through all the potential points
        for d in range(y-1, y+1):
            for c in range(x-1, x+1):
                print(d, c)
                if self.array[d][c] == "M":
                    counter += 1
        self.array[x][y] = counter
    
    def count_mines(self, x, y):
        for a in range(self.array[y]):
            for b in self.array[x]:
                self.check_mines(a,b)

    def print_board(self):
        for row in self.array:
            for col in row:
                print(col, end=' ')
            print()
    # found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853

if __name__ == "__main__":
    array = Array()
    print(array.array)
    # array.generate_board()
    # array.check_mines(array.n, array.m)
    # array.count_mines(array.n, array.m)
    # array.print_board()


'''
[x-1, y-1], [x-1, y], [x-1, y+1],
[x, y-1], [x, y], [x+1, y+1]
[x+1, y-1], [x+1, y], [x+1, y+1]
'''
