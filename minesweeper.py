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
            self.n = 5   # 5 columns and 6 rows
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
        for i in range(0, self.k):
            y, x = random.randint(0, self.n-1), random.randint(0, self.m-1)
            while self.array[x][y] == "M":
                y, x = random.randint(0, self.n-1), random.randint(0, self.m-1)
            self.array[x][y] = "M"
        return self.array

    def check_mines(self, n, m):
        #counter variable 
        counter = 0
        # iterate through all the potential points
        for d in range(m-1, m+2): # on easy, n = 5 but d is zero-indexed; it has to be from n-2 to n+1 to correspond to the right indices
            print('d', d)
            for c in range(n-1, n+2):
                print('c', c)
                if self.array[d][c] == "M":
                    counter += 1
        self.array[n][m] = counter
    
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
    array.generate_board()
    array.check_mines(array.n, array.m)
    array.count_mines(array.n, array.m)
    array.print_board()


'''
[x-1, y-1], [x-1, y], [x-1, y+1],
[x, y-1], [x, y], [x+1, y+1]
[x+1, y-1], [x+1, y], [x+1, y+1]
'''
