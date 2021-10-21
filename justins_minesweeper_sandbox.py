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

def count_mines(x,y):
    


def print_board(a):
    for row in a:
        for col in row:
            print(col, end=' ')
        print()
# found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853


print(print_board(game_board))

[1, 1]
[x-1, y-1], [x-1, y], [x-1, y+1],
[x, y-1], [x, y], [x+1, y+1]
[x+1, y-1], [x+1, y], [x+1, y+1]
