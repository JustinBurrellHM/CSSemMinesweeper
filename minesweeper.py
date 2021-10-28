import random

class Array:
    def __init__(self):
        self.c = 0 # num columns
        self.r = 0 # num rows 
        self.k = 0 # num of mines
        self.array = [] # array that keeps track of where mines are and the mark numbers
        self.user_array = [] # the displayed array

    def set_difficulty(self):
        # takes in user input and determines the dimensions of the board & num. of mines
        difficulty = input("What difficult do you want: [E]asy, [M]edium, or [H]ard? ")
        if difficulty == "E":
            self.c = 5   # 5 columns and 6 rows
            self.r = 6
            self.k = 3
            '''
            creates a blank board of 0's in specified dims 
            '''
            self.array = [[0 for i in range(self.c)] for i in range(self.r)]
            # creates a board of blank squares in specified dims
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
        # randomly generates and places mines on board
        for i in range(0, self.k):
            y, x = random.randint(0, self.c-1), random.randint(0, self.r-1)
            while self.array[x][y] == "M":
                y, x = random.randint(0, self.c-1), random.randint(0, self.r-1)
            self.array[x][y] = "M"
        return self.array

    def check_mines(self, n, m):
        # checks how many mines are directly adjacent to specified point
        counter = 0
        # iterate through all the potential points
        if self.array[m][n] == "M":
            return
        for d in range(m-1, m+2): 
            for c in range(n-1, n+2):
                if self.in_bounds(d,c):
                    if self.array[d][c] == "M":
                        counter += 1
        
        self.array[m][n] = counter 
        return counter
    
    def in_bounds(self, d, c):
        # determines whether idxing is within dims of board
        if d in range(self.r):
            if c in range(self.c):
                return True
        else:
            return False
    
    def count_mines(self, c, r):
        # runs check mines on every point on board
        for m in range(r):
            for n in range(c):
                self.check_mines(m, n)

    def print_board(self):
        # prints the board in a typical grid, instead of a pythonic list of lists
        for row in self.user_array:
            for col in row:
                print(col, end=' ')
            print()
        # print('\n')
        # for row in self.array:
        #     for col in row:
        #         print(col, end=' ')
        #     print()
        
    def mark_board(self):
        '''
        takes in user input for x, y coords of choice at every turn, and takes in the action to perform on
        specified coordinate
        '''
        xinput = int(input("What x coordinate do you want? "))
        yinput = int(input("What y coordinate do you want? "))
        action = str(input("Choose an action: [M]ark, [U]nmark, [R]eveal "))
        if self.in_bounds(xinput, yinput):
            if action == "R":
                # handles the cases where the user reveals a mine, a 0, or a marked number
                if self.array[yinput - 1][xinput - 1] == "M":
                    self.user_array[yinput - 1][xinput - 1] = "M"
                    self.print_board()
                    self.end_game('lost')
                # elif self.array[yinput-1][xinput-1] == 0:
                #     self.zero_chain((yinput-1), (xinput-1))
                #     self.print_board()
                #     self.next_turn(self.r, self.c)
                elif self.array[yinput-1][xinput-1] == 0:
                    self.zero_chain((yinput-1), (xinput-1))
                    self.print_board()
                    self.next_turn(self.r, self.c)
                else:
                    self.user_array[yinput - 1][xinput - 1] = self.array[yinput - 1][xinput - 1]
                    self.print_board()
                    self.next_turn(self.r, self.c)
            if action == "M":
                # shows user a flag on specified coord
                self.user_array[yinput - 1][xinput - 1] = "⚐"
                self.print_board()
                self.next_turn(self.r, self.c)
            if action == 'U':
                # undoes a flagging
                self.user_array[yinput - 1][xinput - 1] = "□"
                self.print_board()
                self.next_turn(self.r, self.c)
    
    def zero_chain(self, n, m):
        # (shld) use recursion to show every 0 in the specified point's immediate vicinity
        if self.in_bounds(m, n):
            self.user_array[m][n] = 0

        if self.array[m][n] != 0:
            return

        for d in range(m-1, m+2):
            for c in range(n-1, n+2):
                if self.in_bounds(d,c):
                    if self.array[d][c] == 0:
                        self.user_array[d][c] = 0
                        self.zero_chain(c, d)
                    else:
                        break



    def next_turn(self, r, c):
        # determines whether the game is over with a win or whether the game should continue with another turn
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
        # starts the game
        self.set_difficulty()
        self.generate_board()
        self.count_mines(self.r, self.c)
        self.print_board()
        self.next_turn(self.r, self.c)
        self.mark_board()


    def end_game(self, status):
        # lets user try again and prints different message depending on win or loss
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