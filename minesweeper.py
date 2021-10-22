import random

class Array:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.k = 0
        self.array = [[0 for i in range(self.n)] for i in range(self.m)]
        self.set_difficulty()
        self.generate_board()
        self.check_mines()
        self.count_mines()
        self.print_board()
    
    def set_difficulty(self):
        difficulty = input("What difficult do you want: Easy, Medium, or Hard? ")
        if difficulty == "Easy":
            self.n = 5
            self.m = 6
            self.k = 3
        elif difficulty == "Medium":
            self.n = 8
            self.m = 8
            self.k = 6
        elif difficulty == "Hard":
            self.n = 12
            self.m = 12
            self.k = 12

    def generate_board(self):
        for i in range(0, self.k):
            y, x = random.randint(0, self.n-1), random.randint(0, self.m-1)
            while self.array[y][x] == "M":
                y, x = random.randint(0, self.n-1), random.randint(0, self.m-1)
            self.array[y][x] = "M"

        return self.array

    def check_mines(self, x, y):
        #counter variable 
        counter = 0
        # iterate through all the potential points
        for d in range(y-1, y+1):
            for c in range(x-1, x+1):
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
    print(array)
'''
[x-1, y-1], [x-1, y], [x-1, y+1],
[x, y-1], [x, y], [x+1, y+1]
[x+1, y-1], [x+1, y], [x+1, y+1]
'''
