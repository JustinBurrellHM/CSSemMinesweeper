import random

def generate_board(n, m, k):
    array = [[0 for i in range(n)] for i in range(m)]
    for i in range(0, k):
        y, x = random.randint(0, n-1), random.randint(0, m-1)
        while array[x][y] == "M":
            y, x = random.randint(0, n-1), random.randint(0, m-1)
        array[x][y] = "M"

    return array

game_board = generate_board(5, 6, 3)

def evaluate_mines(x,y):
    #counter variable 
    counter = 0
    #iterate through all the potential points
    #if that specific coordinate equals M
    # add one to counter
    #turn the original coordinate to counter
'''
[x-1, y-1], [x-1, y], [x-1, y+1],
[x, y-1], [x, y], [x+1, y+1]
[x+1, y-1], [x+1, y], [x+1, y+1]

'''

# def count_mines(a):
    #for each coordinate in the array
    #run evaluate_mines()
    #return new array

def print_board(a):
    for row in a:
        for col in row:
            print(col, end=' ')
        print()
# found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853


print(print_board(game_board))

