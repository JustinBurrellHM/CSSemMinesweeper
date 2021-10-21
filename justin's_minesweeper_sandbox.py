import random
def generate_board(n,m,k):
    array = [[0 for i in range(n)] for i in range(m)]
    for i in range(0,k):
        x, y = random.randint(0,n-1), random.randint(0,m-1)
        '''
        if the x and y values are the same
            randomly pick another x and y 
        do this until they are the same
        '''
        array[x][y] = "M"
    return array

game_board = generate_board(12,12,12)


def print_board(l):
    for row in l:
        for col in row:
            print(col, end=' ')
        print()
# found this solution on https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid/27156853


print(print_board(game_board))

'''
[0,0,0,0]
[0,0,M,0]
[0,0,0,0]
[0,M,0,0]
[0,0,0,0]
'''

