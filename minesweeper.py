import random

class Array:
    def __init__(self):
        self.c = 0 # num columns
        self.r = 0 # num rows 
        self.k = 0 # num of mines
        self.array = []
        self.user_array = []

    def set_difficulty(self):
        difficulty = input("What difficult do you want: [E]asy, [M]edium, or [H]ard? ")
        if difficulty == "E":
            self.c = 5   # 5 columns and 6 rows
            self.r = 6
            self.k = 3
            self.array = [[0 for i in range(self.c)] for i in range(self.r)]
            self.user_array = [["□" for i in range(self.c)] for i in range(self.r)]
        elif difficulty == "M":
            self.c = 8
            self.r = 8
            self.k = 6
            self.array = [[0 for i in range(self.c)] for i in range(self.r)]
            self.user_array = [["□" for i in range(self.c)] for i in range(self.r)]
        elif difficulty == "H":
            self.c = 12
            self.r = 12
            self.k = 12
            self.array = [[0 for i in range(self.c)] for i in range(self.r)]
            self.user_array = [["□" for i in range(self.c)] for i in range(self.r)]
        
    def generate_board(self):
        for i in range(0, self.k):
            y, x = random.randint(0, self.c-1), random.randint(0, self.r-1)
            while self.array[x][y] == "M":
                y, x = random.randint(0, self.c-1), random.randint(0, self.r-1)
            self.array[x][y] = "M"
        return self.array

    def check_mines(self, n, m):
        #counter variable 
        counter = 0
        # iterate through all the potential points
        # self.print_board()
        # print('\n')
        if self.array[m][n] == "M":
            return
        for d in range(m-1, m+2): 
            for c in range(n-1, n+2):
                if self.in_bounds(d,c):
                    if self.array[d][c] == "M":
                        counter += 1
        
        self.array[m][n] = counter #[m-1][n-1] because of 0-idx
        return counter
    
    def in_bounds(self, d, c):
        if d in range(self.r):
            if c in range(self.c):
                return True
        else:
            return False
    
    def count_mines(self, c, r):
        for m in range(r):
            for n in range(c):
                self.check_mines(m, n)

    def print_board(self):
        for row in self.user_array:
            for col in row:
                print(col, end=' ')
            print()
        
    def mark_board(self):
        xinput = int(input("What x coordinate do you want? "))
        yinput = int(input("What y coordinate do you want? "))
        action = str(input("Choose an action: [M]ark, [U]nmark, [R]eveal "))
        if self.in_bounds(xinput, yinput):
            if action == "R":
                if self.array[xinput][yinput] == "M":
                    self.user_array[xinput][yinput] = "M"
                    self.print_board()
                    self.end_game('lost')
                    return
                else:
                    self.user_array[xinput][yinput] = self.array[xinput][yinput]
                    self.print_board()
                    self.next_turn(self.r, self.c)
            if action == "M":
                self.user_array[xinput][yinput] = "⚐"
                self.print_board()
                self.next_turn(self.r, self.c)
            if action == 'U':
                self.user_array[xinput][yinput] = "□"
                self.print_board()
                self.next_turn(self.r, self.c)

            # self.print_board()
            # self.next_turn(self.r, self.c)

    def next_turn(self, r, c): 
        empty_slots = 0
        for m in range(r):
            for n in range(c):
                if self.user_array[m][n] == "□":
                    empty_slots += 1

        if empty_slots != 0:
            self.mark_board()
        else:
            self.end_game('won')

    def start_game(self):
        self.set_difficulty()
        self.generate_board()
        self.count_mines(self.r, self.c)
        self.print_board()
        self.next_turn(self.r, self.c)
        self.mark_board()


    def end_game(self, status):
        if status == "lost":
            print("Oh noooo you hit a mine")
            restart = input('Would you like to try again: Y/N ')
            if  restart == "Y":
                self.start_game()
            else:
                return
        if status == "won":
            print("Yay u won :D")
            restart = input('Would you like to try again: Y/N ')
            if  restart == "Y":
                self.start_game()
            else:
                return
            


    # found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853

if __name__ == "__main__":
    array = Array()
    array.start_game()