import random
def generate_board(n,m,k):
    array = [[0 for i in range(n)] for i in range(m)]
    for i in range(0,k):
        x, y = random.randint(0,n-1), random.randint(0,m-1)
        while array[x][y] == "M":
            x, y = random.randint(0,n-1), random.randint(0,m-1)
        array[x][y] = "M"

    return array

game_board = generate_board(5,6,3)

# def count_mines(a):


def print_board(a):
    for row in a:
        for col in row:
            print(col, end=' ')
        print()
# found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853


print(print_board(game_board))
